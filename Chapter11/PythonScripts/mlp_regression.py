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
  tf.keras.layers.Dense(10, input_shape=[1], activation="relu"),
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(1)
  ])

line_model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(1e-3))
line_model.fit(samples, line_values, epochs=1000, verbose = 0)
line_pred = line_model.predict(samples)

sine_model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(1e-3))
sine_model.fit(samples, sine_values, epochs=1000, verbose = 1)
sine_pred = sine_model.predict(samples)

plt.figure(1)
plt.scatter(samples, line_values, c = 'k')
plt.plot(samples, line_pred, 'b')

plt.figure(2)
plt.scatter(samples , sine_values, c = 'k')
plt.plot(samples, sine_pred, 'b')
plt.show()

line_model.save(osp.join(MODEL_DIR,"nn_line_regression_model_tf"), save_format = "tf")
line_model.save(osp.join(MODEL_DIR, "nn_line_regression_model_keras.h5"), save_format = "h5")