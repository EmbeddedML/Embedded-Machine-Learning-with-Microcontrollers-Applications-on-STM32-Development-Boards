import os
import numpy as np
from scipy.io import wavfile
import cmsisdsp as dsp
import cmsisdsp.mfcc as mfcc
from cmsisdsp.datatype import F32

def create_mfcc_features(recordings_list, FFTSize, sample_rate, numOfMelFilters, numOfDctOutputs, window):
    freq_min = 20
    freq_high = sample_rate / 2
    filtLen, filtPos, packedFilters = mfcc.melFilterMatrix(
        F32, freq_min, freq_high, numOfMelFilters, sample_rate, FFTSize
    )

    dctMatrixFilters = mfcc.dctMatrix(F32, numOfDctOutputs, numOfMelFilters)
    num_samples = len(recordings_list)
    mfcc_features = np.empty((num_samples, numOfDctOutputs * 2), np.float32)
    labels = np.empty(num_samples, dtype = int)

    mfccf32 = dsp.arm_mfcc_instance_f32()

    status = dsp.arm_mfcc_init_f32(
        mfccf32,
        FFTSize,
        numOfMelFilters,
        numOfDctOutputs,
        dctMatrixFilters,
        filtPos,
        filtLen,
        packedFilters,
        window,
    )

    for sample_idx, wav_path in enumerate(recordings_list):
        wav_file = os.path.basename(wav_path)
        file_specs = wav_file.split(".")[0]
        digit, person, recording = file_specs.split("_")
        _, sample = wavfile.read(wav_path)
        sample = sample.astype(np.float32)[:2 * FFTSize]
        if len(sample < 2 * FFTSize):
            sample = np.pad(sample, (0, 2 * FFTSize - len(sample)), "constant", constant_values= 0)
        sample = sample / max(abs(sample))
        first_half = sample[:FFTSize]
        second_half = sample[FFTSize:2*FFTSize]
        tmp = np.zeros(FFTSize + 2)
        first_half_mfcc = dsp.arm_mfcc_f32(mfccf32, first_half, tmp)
        second_half_mfcc = dsp.arm_mfcc_f32(mfccf32, second_half, tmp)
        mfcc_feature = np.concatenate((first_half_mfcc, second_half_mfcc))
        mfcc_features[sample_idx] = mfcc_feature
        labels[sample_idx] = int(digit)
        
    return mfcc_features, labels