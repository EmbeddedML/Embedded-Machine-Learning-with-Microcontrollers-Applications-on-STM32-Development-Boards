import os 
import numpy as np
import cv2
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import keras
from matplotlib import pyplot as plt
from Models.paths import KERAS_MODEL_DIR

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

train_huMoments = np.empty((len(train_images),7))
test_huMoments = np.empty((len(test_images),7))

for train_idx, train_img in enumerate(train_images):
    train_moments = cv2.moments(train_img, True) 
    train_huMoments[train_idx] = cv2.HuMoments(train_moments).reshape(7)

for test_idx, test_img in enumerate(test_images):
    test_moments = cv2.moments(test_img, True) 
    test_huMoments[test_idx] = cv2.HuMoments(test_moments).reshape(7)

features_mean = np.mean(train_huMoments, axis = 0)
features_std = np.std(train_huMoments, axis = 0)
train_huMoments = (train_huMoments - features_mean) / features_std
test_huMoments = (test_huMoments - features_mean) / features_std

model = keras.models.Sequential([
  keras.layers.Dense(1, input_shape = [7], activation = 'sigmoid')
  ])

model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-3),
              loss=keras.losses.BinaryCrossentropy(),
              metrics=[keras.metrics.BinaryAccuracy()])

train_labels[train_labels != 0] = 1
test_labels[test_labels != 0] = 1

model.fit(train_huMoments,
          train_labels, 
          batch_size = 128, 
          epochs=50, 
          class_weight = {0:8, 1:1}, 
          verbose=1,
          workers = 16,
          use_multiprocessing = True)
perceptron_preds = model.predict(test_huMoments)

conf_matrix = confusion_matrix(test_labels, perceptron_preds > 0.5)
cm_display = ConfusionMatrixDisplay(confusion_matrix = conf_matrix)
cm_display.plot()
cm_display.ax_.set_title("Single Neuron Classifier Confusion Matrix")
plt.show()

model.save(os.path.join(KERAS_MODEL_DIR,"hdr_perceptron.h5"))