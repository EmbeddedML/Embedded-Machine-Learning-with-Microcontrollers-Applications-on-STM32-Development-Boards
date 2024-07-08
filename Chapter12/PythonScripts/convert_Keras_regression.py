import os.path as osp
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

DATA_DIR = "regression_data"
MODEL_DIR = "models"

samples = np.load(osp.join(DATA_DIR, "reg_samples.npy"))
line_values = np.load(osp.join(DATA_DIR, "reg_line_values.npy"))
sine_values = np.load(osp.join(DATA_DIR, "reg_sine_values.npy"))

line_model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(10, input_shape=[1], activation="relu"),
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(1)
  ])

sine_model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(100, input_shape=[1], activation="relu"),
  tf.keras.layers.Dense(100, activation="relu"),
  tf.keras.layers.Dense(1)
  ])

line_model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(1e-3))
line_model.fit(samples, line_values, epochs=1000, verbose = 0)

sine_model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(1e-3))
sine_model.fit(samples, sine_values, epochs=1000, verbose = 1)

line_model.save(osp.join(MODEL_DIR, "nn_line_regression_model.keras"))
sine_model.save(osp.join(MODEL_DIR, "nn_sine_regression_model.keras"))

# Convert the Keras line model to TF Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(line_model)
tflite_model = converter.convert()

# Save the TF Lite model.
with open('models/nn_line_regression_model.tflite', 'wb') as f:
  f.write(tflite_model)

# Convert the Keras sine model to TF Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(sine_model)
tflite_model = converter.convert()

# Save the TF Lite model.
with open('models/nn_sine_regression_model.tflite', 'wb') as f:
  f.write(tflite_model)
