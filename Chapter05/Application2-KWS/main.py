import os
import scipy.signal as sig
from .mfcc_func import create_mfcc_features
from Data.paths import FSDD_PATH

recordings_list = [os.path.join(FSDD_PATH, rec_path) for rec_path in os.listdir(FSDD_PATH)]

FFTSize = 1024
sample_rate = 8000
numOfMelFilters = 10
numOfDctOutputs = 13
window = sig.get_window("hamming", FFTSize)
create_mfcc_features(recordings_list, FFTSize, sample_rate, numOfMelFilters, numOfDctOutputs, window)