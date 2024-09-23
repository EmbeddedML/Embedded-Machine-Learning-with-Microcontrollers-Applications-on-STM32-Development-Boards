import os
import tensorflow as tf
from keras.models import load_model
from Common.tflite2cc import convert_tflite2cc
from Models.paths import KERAS_MODEL_DIR, TFLITE_EXPORT_DIR, TFLITE_MODEL_DIR

model = load_model(os.path.join(KERAS_MODEL_DIR,"hdr_perceptron.h5"))
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
tflite_save_path = os.path.join(TFLITE_MODEL_DIR, "hdr_perceptron.tflite")
with open(tflite_save_path, "wb") as tflite_file:
    tflite_file.write(tflite_model)
tflite_export_path = os.path.join(TFLITE_EXPORT_DIR, "hdr_perceptron")
convert_tflite2cc(tflite_model = tflite_model, c_out= tflite_export_path)