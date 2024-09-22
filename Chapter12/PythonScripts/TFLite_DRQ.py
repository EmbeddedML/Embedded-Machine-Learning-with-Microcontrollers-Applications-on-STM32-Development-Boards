import os
import tensorflow as tf
from Models.paths import SAVED_MODEL_DIR, TFLITE_MODEL_DIR

# Convert a saved model
saved_model_path = os.path.join(SAVED_MODEL_DIR, "nn_classification")
dyn_range_model_path = os.path.join(TFLITE_MODEL_DIR, "quantized_model_dyn_range.tflite")

# Dynamic range quantization
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_path)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model_quant = converter.convert()

# Save the model.
with open(dyn_range_model_path, "wb") as f:
    f.write(tflite_model_quant)
