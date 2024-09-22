import os
import tensorflow as tf
import numpy as np
from Data.paths import REGRESSION_DATA_DIR
from Models.paths import KERAS_MODEL_DIR, TFLITE_MODEL_DIR


samples = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_samples.npy"))
line_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_line_values.npy"))
sine_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_sine_values.npy"))

line_model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Dense(10, input_shape=[1], activation="relu"),
        tf.keras.layers.Dense(10, activation="relu"),
        tf.keras.layers.Dense(1),
    ]
)

sine_model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Dense(100, input_shape=[1], activation="relu"),
        tf.keras.layers.Dense(100, activation="relu"),
        tf.keras.layers.Dense(1),
    ]
)

line_model.compile(loss="mean_squared_error", optimizer=tf.keras.optimizers.Adam(1e-3))
line_model.fit(samples, line_values, epochs=1000, verbose=0)

sine_model.compile(loss="mean_squared_error", optimizer=tf.keras.optimizers.Adam(1e-3))
sine_model.fit(samples, sine_values, epochs=1000, verbose=1)

line_model.save(os.path.join(KERAS_MODEL_DIR, "nn_line_regression.keras"))
sine_model.save(os.path.join(KERAS_MODEL_DIR, "nn_sine_regression.keras"))

# Convert the Keras line model to TF Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(line_model)
tflite_model = converter.convert()

with open(os.path.join(TFLITE_MODEL_DIR, "nn_line_regression.tflite"), "wb") as f:
    f.write(tflite_model)

# Convert the Keras sine model to TF Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(sine_model)
tflite_model = converter.convert()

with open(os.path.join(TFLITE_MODEL_DIR, "nn_sine_regression.tflite"), "wb") as f:
    f.write(tflite_model)
