import os
import tensorflow as tf
from Models.paths import SAVED_MODEL_DIR, TFLITE_MODEL_DIR

# Convert a saved model
saved_model_dir = os.path.join(SAVED_MODEL_DIR, "nn_classification")
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Save the TF Lite model
with open(os.path.join(TFLITE_MODEL_DIR, "nn_classification_saved.tflite"), "wb") as f:
    f.write(tflite_model)
