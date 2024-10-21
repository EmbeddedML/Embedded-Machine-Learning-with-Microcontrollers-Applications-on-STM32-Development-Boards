import os
import tensorflow as tf
from keras.models import load_model
from Common.tflite2cc import convert_tflite2cc
from Models.paths import KERAS_MODEL_DIR, TFLITE_EXPORT_DIR

model = load_model(os.path.join(KERAS_MODEL_DIR, "temperature_pred_mlp.h5"))
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
convert_tflite2cc(tflite_model, os.path.join("temperature_pred_mlp"))