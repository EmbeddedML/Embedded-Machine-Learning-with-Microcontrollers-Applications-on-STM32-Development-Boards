import os
import scipy.signal as sig
from mfcc_func import create_mfcc_features
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import sklearn2c
from matplotlib import pyplot as plt

RECORDINGS_DIR = "recordings"
recordings_list = [(RECORDINGS_DIR, recording_path) for recording_path in os.listdir(RECORDINGS_DIR)]

FFTSize = 1024
sample_rate = 8000
numOfMelFilters = 20
numOfDctOutputs = 13
window = sig.get_window("hamming", FFTSize)
test_list = {record for record in recordings_list if "yweweler" in record[1]}
train_list = set(recordings_list) - test_list
train_mfcc_features, train_labels = create_mfcc_features(train_list, FFTSize, sample_rate, numOfMelFilters, numOfDctOutputs, window)
test_mfcc_features, test_labels = create_mfcc_features(test_list, FFTSize, sample_rate, numOfMelFilters, numOfDctOutputs, window)

knn =sklearn2c.KNNClassifier(n_neighbors = 3)
knn.train(train_mfcc_features, train_labels)
knn_preds = knn.predict(test_mfcc_features)

conf_matrix = confusion_matrix(test_labels, knn_preds)
cm_display = ConfusionMatrixDisplay(confusion_matrix = conf_matrix, display_labels = knn.class_names)
cm_display.plot()
cm_display.ax_.set_title("KNN Classifier Confusion Matrix")
plt.show()

knn.export("knn_mfcc_config")
