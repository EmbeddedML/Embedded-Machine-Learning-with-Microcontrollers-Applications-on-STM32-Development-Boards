import numpy as np
import scipy.signal as sig

FFTSize = 1024
numOfDctOutputs = 13

sample_rate = 8000
freq_min = 0
freq_high = sample_rate / 2
numOfMelFilters = 10
frame_step = 512
window = sig.hamming(FFTSize, sym=False)


def frequencyToMelSpace(freq):
    return 1127.0 * np.log(1.0 + freq / 700.0)


def melSpaceToFrequency(mels):
    return 700.0 * (np.exp(mels / 1127.0) - 1.0)


def mydct(numOfDctOutputs, numOfMelFilters):
    result = np.zeros((numOfDctOutputs * numOfMelFilters), np.float32)
    norm_mels = np.sqrt(2.0 / numOfMelFilters)
    for mel_idx in range(numOfMelFilters):
        for dct_idx in range(numOfDctOutputs):
            s = (mel_idx + 0.5) / numOfMelFilters
            result[dct_idx * numOfMelFilters + mel_idx] = (np.cos(dct_idx * np.pi * s) * norm_mels)

    return result


def myMel(fmin, fmax, n_mels, fs, FFTSize):
    filters = np.zeros((n_mels, int(FFTSize / 2 + 1)), np.float32)
    filtPos = np.zeros(n_mels, dtype=np.uint16)
    filtLen = np.zeros(n_mels, dtype=np.uint16)
    spectrogram_mel = np.zeros(int(FFTSize // 2), dtype=np.float32)
    packedFilters = []

    fmin_mel = frequencyToMelSpace(fmin)
    fmax_mel = frequencyToMelSpace(fmax)
    freq_step = (fs / 2) / int(FFTSize // 2)

    for freq_idx in range(1, int(FFTSize // 2 + 1)):
        linear_freq = freq_idx * freq_step
        spectrogram_mel[freq_idx - 1] = frequencyToMelSpace(linear_freq)

    mel_step = (fmax_mel - fmin_mel) / (n_mels + 1)
    for mel_idx in range(n_mels):
        mel = mel_step * mel_idx
        startFound = False
        for freq_idx in range(int(FFTSize / 2)):
            upper = (spectrogram_mel[freq_idx] - mel) / mel_step
            lower = (mel - spectrogram_mel[freq_idx]) / mel_step + 2
            filter_val = max(0, min(upper, lower))
            filters[mel_idx, freq_idx + 1] = filter_val
            if not startFound and filter_val != 0.0:
                startFound = True
                startPos = freq_idx + 1

            if startFound and filter_val == 0.0:
                endPos = freq_idx
                break
        filtLen[mel_idx] = (endPos - startPos + 1)
        filtPos[mel_idx] = startPos
        packedFilters = np.hstack((packedFilters, filters[mel_idx, startPos : endPos + 1]), dtype=np.float32)

    return filtLen, filtPos, packedFilters

myLen, myPos, myFilters = myMel(freq_min, freq_high, numOfMelFilters, sample_rate, FFTSize)
myres = mydct(numOfDctOutputs, numOfMelFilters)