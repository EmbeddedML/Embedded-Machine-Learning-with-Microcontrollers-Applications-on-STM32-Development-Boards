import os
import scipy.signal as sig
from mfcc_func import create_mfcc_features

RECORDINGS_DIR = "recordings"
recordings_list = [os.path.join(RECORDINGS_DIR, recording_path) for recording_path in os.listdir(RECORDINGS_DIR)]

FFTSize = 1024
sample_rate = 8000
numOfMelFilters = 10
numOfDctOutputs = 13
window = sig.get_window("hamming", FFTSize)
create_mfcc_features(recordings_list, FFTSize, sample_rate, numOfMelFilters, numOfDctOutputs, window)
