import os
import numpy as np
import tensorflow as tf
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import KERAS_MODEL_DIR, SAVED_MODEL_DIR,TFLITE_MODEL_DIR

saved_model_dir = os.path.join(SAVED_MODEL_DIR, 'nn_classification')
pruned_model_path = os.path.join(KERAS_MODEL_DIR, "nn_classification_pruned.h5")
pruned_lite_path = os.path.join(TFLITE_MODEL_DIR, "nn_classification_pruned.tflite")
pruned_dyn_lite_path = os.path.join(TFLITE_MODEL_DIR, "pruned_quant_model_dyn_range.tflite")
pruned_fiq_lite_path = os.path.join(TFLITE_MODEL_DIR, 'pruned_quant_model_int_w_float.tflite')
model = tf.keras.models.load_model(saved_model_dir)
model.summary()

pruned_model=tf.keras.models.load_model(pruned_model_path)
pruned_model.summary()

converter = tf.lite.TFLiteConverter.from_keras_model(pruned_model)
pruned_tflite_model = converter.convert()

# Save the model
with open(pruned_lite_path, 'wb') as f:
  f.write(pruned_tflite_model)

# Dynamic range quantization
converter = tf.lite.TFLiteConverter.from_keras_model(pruned_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model_quant = converter.convert()

# Save the model
with open(pruned_dyn_lite_path, 'wb') as f:
  f.write(tflite_model_quant)

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))

# Convert train_samples to float32 format
train_samples = train_samples.astype(np.float32)

def representative_dataset():
  for input_value in tf.data.Dataset.from_tensor_slices(train_samples).batch(1).take(100):
    # Model has only one input so each data point has one element.
    yield [input_value]

# Full integer quantization
# Integer with float fallback (using default float input/output)
converter = tf.lite.TFLiteConverter.from_keras_model(pruned_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
tflite_model_quant = converter.convert()

# Save the model.
with open(pruned_fiq_lite_path, 'wb') as f:
  f.write(tflite_model_quant)