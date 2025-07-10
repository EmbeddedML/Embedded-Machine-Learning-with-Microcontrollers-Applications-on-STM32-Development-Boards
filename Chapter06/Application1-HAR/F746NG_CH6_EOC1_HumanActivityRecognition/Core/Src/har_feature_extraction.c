/*
 * har_feature_extraction.c
 *
 *  Created on: 21 Mar 2024
 *      Author: Eren Atmaca, Berkan Höke
 */
#include "har_feature_extraction.h"

static float fft_output[3][VECTOR_LEN];		/* FFT Output			*/
static float fft_sd[3]; 					/* Standard Deviation	*/
static float fft_abs[3][VECTOR_LEN/2];		/* FFT Absolute Value	*/

/*
 * @brief Performs feature extraction for human activity detection.
 * @param acc_data 3 axis accelerometer vectors of size VECTOR_LEN
 * @param output Function's output
 * @retval 0 if successful
 */
int8_t har_extract_features(float32_t acc_data[3][VECTOR_LEN], HAR_FtrExtOutput *output)
{

	float32_t sma_x = 0, sma_y = 0, sma_z = 0, sma = 0;
	float32_t x_mean = 0, y_mean = 0, z_mean = 0;
	int32_t x_pos = 0, y_pos = 0, z_pos = 0;

	for(uint32_t i = 0; i < VECTOR_LEN; i++)
	{
		x_mean += acc_data[0][i];
		y_mean += acc_data[1][i];
		z_mean += acc_data[2][i];
		x_pos += (acc_data[0][i] > 0);
		y_pos += (acc_data[1][i] > 0);
		z_pos += (acc_data[2][i] > 0);
	}

	x_mean /= VECTOR_LEN;
	y_mean /= VECTOR_LEN;
	z_mean /= VECTOR_LEN;

	arm_rfft_fast_instance_f32 fft;
	arm_status res = arm_rfft_fast_init_f32(&fft, VECTOR_LEN);
	if (res != 0)
	{
		return -1;
	}

	for(int32_t i = 0; i < 3; i++)
	{
		arm_rfft_fast_f32(&fft, &acc_data[i][0], &fft_output[i][0], 0);
		arm_cmplx_mag_f32(&fft_output[i][0], &fft_abs[i][0], VECTOR_LEN/2);
		arm_std_f32(&fft_abs[i][1], ((VECTOR_LEN/2) - 1), &fft_sd[i]);
	}

	for(int32_t i = 1; i < VECTOR_LEN/2; i++)
	{
		sma_x += fft_abs[0][i];
		sma_y += fft_abs[1][i];
		sma_z += fft_abs[2][i];
	}

	sma = (sma_x + sma_y + sma_z) / (VECTOR_LEN/2);
	output->fft_sd_x = fft_sd[0];
	output->fft_sd_y = fft_sd[1];
	output->fft_sd_z = fft_sd[2];
	output->sma = sma;
	output->x_mean = x_mean;
	output->y_mean = y_mean;
	output->z_mean = z_mean;
	output->x_pos = x_pos;
	output->y_pos = y_pos;
	output->z_pos = z_pos;
	return 0;
}


