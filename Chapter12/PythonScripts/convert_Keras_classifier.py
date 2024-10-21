import os
import numpy as np
import tensorflow as tf
import keras
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import SAVED_MODEL_DIR, KERAS_MODEL_DIR, TFLITE_MODEL_DIR

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_labels.npy"))
test_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_test_samples.npy"))
test_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_test_labels.npy"))

model = keras.models.Sequential(
    [
        keras.layers.Dense(20, input_shape=[2], activation="relu"),
        keras.layers.Dense(1, activation="sigmoid"),
    ]
)

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss=keras.losses.BinaryCrossentropy(),
    metrics=[keras.metrics.BinaryAccuracy(), keras.metrics.FalseNegatives()],
)

model.fit(
    train_samples,
    train_labels,
    validation_data=(test_samples, test_labels),
    epochs=50,
    verbose=1,
)
print("Finished training the model")

model.save(os.path.join(KERAS_MODEL_DIR, "nn_classification.keras"))
model.save(os.path.join(SAVED_MODEL_DIR, "nn_classification"), save_format="tf")
model.save(os.path.join(KERAS_MODEL_DIR, "nn_classification.h5"), save_format="h5")

# Convert the Keras model to TF Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TF Lite model
with open(os.path.join(TFLITE_MODEL_DIR, "nn_classification.tflite"), "wb") as f:
    f.write(tflite_model)
