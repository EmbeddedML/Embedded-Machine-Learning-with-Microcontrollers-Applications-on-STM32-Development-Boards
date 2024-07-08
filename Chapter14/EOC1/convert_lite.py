import tensorflow as tf
import keras
from tflite2cc import convert_tflite2cc

TFLITE_MODEL_PATH = "kws_rnn_model.tflite"
kws_rnn_model = keras.models.load_model("kws_rnn_model.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(kws_rnn_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS]
kws_rnn_lite = converter.convert()

with open(TFLITE_MODEL_PATH, "wb") as tflite_file:
    tflite_file.write(kws_rnn_lite)

convert_tflite2cc(TFLITE_MODEL_PATH, "kws_rnn_model")
