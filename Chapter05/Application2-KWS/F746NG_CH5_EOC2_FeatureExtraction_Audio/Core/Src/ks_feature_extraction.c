/*
 * ks_feature_extraction.c
 *
 *  Created on: Mar 23, 2024
 *      Author: Eren Atmaca, Berkan Höke
 */
#include "ks_feature_extraction.h"

#include <stdbool.h>
#include <math.h>



arm_mfcc_instance_f32 mfcc;

uint32_t filterPos[nbMelFilters];
uint32_t filterLengths[nbMelFilters];
float32_t dctCoefs[nbMelFilters];
//float32_t filterCoefs[nbMelFilters];
float32_t windowCoefs[fftLen];
float32_t dctMatrix[nbDctOutputs * nbMelFilters];
float32_t tmpBuf[1024 + 2];
float32_t packedFilters[1024];

static float32_t ks_mfcc_freq2mel(float32_t freq);
static float32_t ks_mfcc_mel2freq(float32_t mel);
static void ks_mfcc_create_dct_matrix(void);
static void ks_mfcc_create_mel_fbank(void);


int8_t ks_mfcc_init(void)
{
	arm_hamming_f32(windowCoefs, 1024);
//	for (uint32_t i = 0; i < fftLen; i++)
//	{
//		windowCoefs[i] = 0.5 - 0.5 * arm_cos_f32(2 * PI * ((float32_t) i) / ((float32_t) fftLen));
//	}
	ks_mfcc_create_mel_fbank();
	ks_mfcc_create_dct_matrix();
	arm_mfcc_init_1024_f32(&mfcc, nbMelFilters, nbDctOutputs, dctMatrix, filterPos, filterLengths, packedFilters, windowCoefs);
	return 0;
}

int8_t ks_mfcc_extract_features(float32_t *input, float32_t *output)
{
	arm_mfcc_f32(&mfcc, input, output, tmpBuf);
	return 0;
}

static float32_t ks_mfcc_freq2mel(float32_t freq)
{
	float32_t in = (1.0f + freq / 700.0f), out;
	arm_vlog_f32(&in, &out, 1);
	return (1127.0f * out);

}

static float32_t ks_mfcc_mel2freq(float32_t mel)
{
	float32_t in = (mel / 1127.0f), out;
	arm_vexp_f32(&in, &out, 1);
	return (700.0f * (out - 1.0f));
}

static void ks_mfcc_create_dct_matrix(void)
{
	//arm_dct4_init_f32(S, S_RFFT, S_CFFT, N, Nby2, normalize)
	float32_t norm_mels;
	arm_sqrt_f32(2.0f/nbMelFilters, &norm_mels);
	for (int mel_idx = 0; mel_idx < nbMelFilters; mel_idx++)
	{
		for (int dct_idx = 0; dct_idx < nbDctOutputs; dct_idx++)
		{
			float s = (mel_idx + 0.5) / nbMelFilters;
			dctMatrix[dct_idx * nbMelFilters + mel_idx] = (arm_cos_f32(dct_idx * M_PI * s) * norm_mels);
		}
	}
}

float32_t filters[nbMelFilters][fftLen / 2 + 1];
float32_t spectrogram_mel[fftLen / 2];

static void ks_mfcc_create_mel_fbank(void)
{
	int32_t half_fft_size = fftLen / 2;


	float32_t fmin_mel = ks_mfcc_freq2mel(MEL_LOW_FREQ);
	float32_t fmax_mel = ks_mfcc_freq2mel(MEL_HIGH_FREQ);
	float32_t freq_step = ((float32_t)SAMP_FREQ / (float32_t)fftLen);

	for (uint32_t freq_idx = 1; freq_idx < half_fft_size + 1; freq_idx++)
	{
		float32_t linear_freq = freq_idx * freq_step;
		spectrogram_mel[freq_idx - 1] = ks_mfcc_freq2mel(linear_freq);
	}

	float32_t mel_step = (fmax_mel - fmin_mel) / (nbMelFilters + 1);
	uint32_t totalLen = 0;
	for (uint32_t mel_idx = 0; mel_idx < nbMelFilters; mel_idx++)
	{
		float32_t mel = mel_step * mel_idx + fmin_mel;
		bool startFound = false;
		uint32_t startPos = 0, endPos = 0, curLen = 0;
		for (uint32_t freq_idx = 0; freq_idx < half_fft_size; freq_idx++)
		{
			float32_t upper = (spectrogram_mel[freq_idx] - mel) / mel_step;
			float32_t lower = ((mel + 2.0f * mel_step) - spectrogram_mel[freq_idx]) / mel_step; //+ 2.0f;
			if (lower < 1e-5)
			{
				lower = 0;
			}
			float32_t filter_val = fmaxf(0.0f, fminf(upper, lower));

			filters[mel_idx][freq_idx + 1] = filter_val;
			if (!startFound && (filter_val != 0.0f))
			{
				startFound = true;
				startPos = freq_idx + 1;
			}

			else if (startFound && (filter_val == 0.0f))
			{
				endPos = freq_idx;
				break;
			}
		}
		curLen = endPos - startPos + 1;
		filterLengths[mel_idx] = (endPos - startPos + 1);
		filterPos[mel_idx] = startPos;

//		windowCoefs = realloc(windowCoefs, (totalLen + curLen) * sizeof(float));
//		if (windowCoefs == NULL)
//		{
//			//printf("Memory allocation failed\n");
//			return -1;
//		}

		memcpy(packedFilters + totalLen, &filters[mel_idx][startPos], curLen * sizeof(float32_t));
		totalLen += curLen;
	}
}
