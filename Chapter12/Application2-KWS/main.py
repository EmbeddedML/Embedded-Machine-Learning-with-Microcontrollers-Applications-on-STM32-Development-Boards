import os
import tensorflow as tf
from keras.models import load_model
from Common.tflite2cc import convert_tflite2cc
from Models.paths import KERAS_MODEL_DIR, TFLITE_EXPORT_DIR

model_path = os.path.join(KERAS_MODEL_DIR,"kws_mlp.h5")
model = load_model(model_path)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
convert_tflite2cc(tflite_model, os.path.join(TFLITE_EXPORT_DIR,"kws_mlp"))