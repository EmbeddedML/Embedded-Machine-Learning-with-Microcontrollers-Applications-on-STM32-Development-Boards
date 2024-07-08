import os.path as osp
import numpy as np
import tensorflow as tf

saved_model_dir='models/nn_classification_model_tf'

model = tf.keras.models.load_model(saved_model_dir)
model.summary()

clustered_model=tf.keras.models.load_model('models/clustered_model.h5')
clustered_model.summary()

converter = tf.lite.TFLiteConverter.from_keras_model(clustered_model)
clustered_tflite_model = converter.convert()

# Save the model
with open('models/clustered_model.tflite', 'wb') as f:
  f.write(clustered_tflite_model)

# Clustering and Quantization

# Dynamic range quantization
converter = tf.lite.TFLiteConverter.from_keras_model(clustered_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model_quant = converter.convert()

# Save the model
with open('models/clustered_quant_model_dyn_range.tflite', 'wb') as f:
  f.write(tflite_model_quant)

DATA_DIR = "classification_data"

train_samples = np.load(osp.join(DATA_DIR, "cls_train_samples.npy"))

# Convert train_samples to float32 format
train_samples = train_samples.astype(np.float32)

def representative_dataset():
  for input_value in tf.data.Dataset.from_tensor_slices(train_samples).batch(1).take(100):
    # Model has only one input so each data point has one element.
    yield [input_value]

# Full integer quantization
# Integer with float fallback (using default float input/output)
converter = tf.lite.TFLiteConverter.from_keras_model(clustered_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
tflite_model_quant = converter.convert()

# Save the model
with open('models/clustered_quant_model_int_w_float.tflite', 'wb') as f:
  f.write(tflite_model_quant)