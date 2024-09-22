import os
import tensorflow as tf
from tflite2cc import convert_tflite2cc
from Models.paths import SAVED_MODEL_DIR, TFLITE_MODEL_DIR, TFLITE_EXPORT_DIR

# Convert a saved model
saved_model_path = os.path.join(SAVED_MODEL_DIR, "nn_classification")
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_path)
tflite_model = converter.convert()

tflite_model_file = os.path.join(TFLITE_MODEL_DIR, "nn_classification_model.tflite")

# Save the TF Lite model
with open(tflite_model_file, "wb") as f:
    f.write(tflite_model)

tflite_export_path = os.path.join(TFLITE_EXPORT_DIR, "nn_classification")

convert_tflite2cc(tflite_model, c_out=tflite_export_path)