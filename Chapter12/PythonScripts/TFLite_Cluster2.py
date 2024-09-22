import os
import numpy as np
import tensorflow as tf
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import SAVED_MODEL_DIR, KERAS_MODEL_DIR, TFLITE_MODEL_DIR

saved_model_path = os.path.join(SAVED_MODEL_DIR, "nn_classification")
clustered_model_path = os.path.join(KERAS_MODEL_DIR,"clustered_model.h5")
tflite_model_path =  os.path.join(TFLITE_MODEL_DIR, "clustered_model.tflite")
clustered_quant_path = os.path.join(TFLITE_MODEL_DIR, "clustered_quant_model_dyn_range.tflite")
clustered_int_w_float_path = os.path.join("clustered_quant_model_int_w_float.tflite")

model = tf.keras.models.load_model(saved_model_path)
model.summary()

clustered_model = tf.keras.models.load_model(clustered_model_path)
clustered_model.summary()

converter = tf.lite.TFLiteConverter.from_keras_model(clustered_model)
clustered_tflite_model = converter.convert()

# Save the model
with open(tflite_model_path, "wb") as f:
    f.write(clustered_tflite_model)

# Dynamic range quantization
converter = tf.lite.TFLiteConverter.from_keras_model(clustered_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model_quant = converter.convert()

# Save the model
with open(clustered_quant_path, "wb") as f:
    f.write(tflite_model_quant)

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))
# Convert train_samples to float32 format
train_samples = train_samples.astype(np.float32)


def representative_dataset():
    for input_value in (
        tf.data.Dataset.from_tensor_slices(train_samples).batch(1).take(100)
    ):
        # Model has only one input so each data point has one element.
        yield [input_value]


# Full integer quantization
# Integer with float fallback (using default float input/output)
converter = tf.lite.TFLiteConverter.from_keras_model(clustered_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
tflite_model_quant = converter.convert()

# Save the model
with open(clustered_int_w_float_path, "wb") as f:
    f.write(tflite_model_quant)
