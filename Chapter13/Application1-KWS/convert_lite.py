import os
import tensorflow as tf
import keras
from tflite2cc import convert_tflite2cc
from Models.paths import TFLITE_MODEL_DIR, TFLITE_EXPORT_DIR, KERAS_MODEL_DIR

tflite_model_path = os.path.join(TFLITE_MODEL_DIR, "kws_cnn.tflite")
kws_cnn_model = keras.models.load_model(os.path.join(KERAS_MODEL_DIR, "kws_cnn.h5"))
converter = tf.lite.TFLiteConverter.from_keras_model(kws_cnn_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
kws_cnn_lite = converter.convert()

with open(tflite_model_path, "wb") as tflite_file:
    tflite_file.write(kws_cnn_lite)

convert_tflite2cc(tflite_model_path, os.path.join(TFLITE_EXPORT_DIR, "kws_cnn"))
