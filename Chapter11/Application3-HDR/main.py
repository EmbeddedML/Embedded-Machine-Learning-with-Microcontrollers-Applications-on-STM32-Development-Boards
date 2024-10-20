import os
import numpy as np
import cv2
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import keras
from keras.callbacks import EarlyStopping, ModelCheckpoint
from matplotlib import pyplot as plt
from Models.paths import KERAS_MODEL_DIR

model_save_path = os.path.join(KERAS_MODEL_DIR, "hdr_mlp.h5")
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

train_huMoments = np.empty((len(train_images),7))
test_huMoments = np.empty((len(test_images),7))

for train_idx, train_img in enumerate(train_images):
    train_moments = cv2.moments(train_img, True) 
    train_huMoments[train_idx] = cv2.HuMoments(train_moments).reshape(7)

for test_idx, test_img in enumerate(test_images):
    test_moments = cv2.moments(test_img, True) 
    test_huMoments[test_idx] = cv2.HuMoments(test_moments).reshape(7)

model = keras.models.Sequential([
  keras.layers.Dense(100, input_shape=[7], activation="relu"),
  keras.layers.Dense(100, activation="relu"),
  keras.layers.Dense(10, activation = "softmax")
  ])

categories = np.unique(test_labels)
model.compile(loss=keras.losses.SparseCategoricalCrossentropy(), optimizer=keras.optimizers.Adam(1e-4))
mc_callback = ModelCheckpoint(model_save_path)
es_callback = EarlyStopping("loss", patience = 5)
model.fit(train_huMoments, train_labels, epochs=1000, verbose = 1, callbacks=[mc_callback, es_callback])
model = keras.models.load_model(model_save_path)
nn_preds = model.predict(test_huMoments)
predicted_classes = np.argmax(nn_preds, axis = 1)

conf_matrix = confusion_matrix(test_labels, predicted_classes)
cm_display = ConfusionMatrixDisplay(confusion_matrix = conf_matrix, display_labels= categories)
cm_display.plot()
cm_display.ax_.set_title("Neural Network Confusion Matrix")
plt.show()