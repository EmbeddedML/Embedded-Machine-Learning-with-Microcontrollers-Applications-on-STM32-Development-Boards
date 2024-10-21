import os
import numpy as np
import tensorflow as tf
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import SAVED_MODEL_DIR, KERAS_MODEL_DIR

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_labels.npy"))
test_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_test_samples.npy"))
test_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_test_labels.npy"))

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(20, input_shape=[2], activation='relu'),
  tf.keras.layers.Dense(1, activation = 'sigmoid')
  ])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(),
                       tf.keras.metrics.FalseNegatives()])
  

model.fit(train_samples, train_labels, validation_data = (test_samples, test_labels), epochs=50, verbose=1)
print("Finished training the model")

model.save(os.path.join(SAVED_MODEL_DIR,"nn_classification_model_tf"), save_format = "tf")
model.save(os.path.join(KERAS_MODEL_DIR, "nn_classification_model_keras.h5"), save_format = "h5")
model.evaluate(test_samples, test_labels)