import os
import scipy.signal as sig
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib import pyplot as plt
import keras
from .mfcc_func import create_mfcc_features
from Data.paths import FSDD_PATH
from Models.paths import KERAS_MODEL_DIR

recordings_list = [os.path.join(FSDD_PATH, rec_path) for rec_path in os.listdir(FSDD_PATH)]

FFTSize = 1024
sample_rate = 8000
numOfMelFilters = 20
numOfDctOutputs = 13
window = sig.get_window("hamming", FFTSize)
test_list = {record for record in recordings_list if "yweweler" in os.path.basename(record)}
train_list = set(recordings_list) - test_list
train_mfcc_features, train_labels = create_mfcc_features(train_list, FFTSize, sample_rate, numOfMelFilters, numOfDctOutputs, window)
test_mfcc_features, test_labels = create_mfcc_features(test_list, FFTSize, sample_rate, numOfMelFilters, numOfDctOutputs, window)

model = keras.models.Sequential([
  keras.layers.Dense(1, input_shape = [numOfDctOutputs * 2], activation = 'sigmoid')
  ])

model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-3),
              loss=keras.losses.BinaryCrossentropy(),
              metrics=[keras.metrics.BinaryAccuracy(),
                       keras.metrics.FalseNegatives()])

train_labels[train_labels != 0] = 1
test_labels[test_labels != 0] = 1

model.fit(train_mfcc_features, train_labels, epochs=50, verbose=1, class_weight = {0:10., 1:1.})
perceptron_preds = model.predict(test_mfcc_features)

conf_matrix = confusion_matrix(test_labels, perceptron_preds > 0.5)
cm_display = ConfusionMatrixDisplay(confusion_matrix = conf_matrix)
cm_display.plot()
cm_display.ax_.set_title("Single Neuron Classifier Confusion Matrix")
plt.show()

model.save(os.path.join(KERAS_MODEL_DIR, "kws_perceptron.h5"))