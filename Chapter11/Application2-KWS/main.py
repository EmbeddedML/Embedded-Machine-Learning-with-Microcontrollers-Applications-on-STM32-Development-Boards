import os
import numpy as np
import scipy.signal as sig
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import OneHotEncoder
import keras
from matplotlib import pyplot as plt
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
  keras.layers.Dense(100, input_shape=[26], activation="relu"),
  keras.layers.Dense(100, activation="relu"),
  keras.layers.Dense(10, activation = "softmax")
  ])

ohe = OneHotEncoder()
train_labels_ohe = ohe.fit_transform(train_labels.reshape(-1, 1)).toarray()
categories, test_labels = np.unique(test_labels, return_inverse = True)
model.compile(loss=keras.losses.CategoricalCrossentropy(), optimizer=keras.optimizers.Adam(1e-3))
model.fit(train_mfcc_features, train_labels_ohe, epochs=100, verbose = 1)
nn_preds = model.predict(test_mfcc_features)
predicted_classes = np.argmax(nn_preds, axis = 1)

conf_matrix = confusion_matrix(test_labels, predicted_classes)
cm_display = ConfusionMatrixDisplay(confusion_matrix = conf_matrix, display_labels=categories)
cm_display.plot()
cm_display.ax_.set_title("Neural Network Confusion Matrix")
plt.show()

model.save(os.path.join(KERAS_MODEL_DIR, "kws_mlp.h5"))
