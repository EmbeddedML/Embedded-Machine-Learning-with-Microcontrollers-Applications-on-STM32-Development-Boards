import os
import tensorflow as tf
from keras.models import load_model
from Common.tflite2cc import convert_tflite2cc
from Models.paths import KERAS_MODEL_DIR, TFLITE_EXPORT_DIR, TFLITE_MODEL_DIR

model_path = os.path.join(KERAS_MODEL_DIR,"hdr_mlp.h5")
model = load_model(model_path)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open(os.path.join(TFLITE_MODEL_DIR, "hdr_mlp.tflite"), "wb") as f:
    f.write(tflite_model)

convert_tflite2cc(tflite_model, os.path.join(TFLITE_EXPORT_DIR, "hdr_mlp"))