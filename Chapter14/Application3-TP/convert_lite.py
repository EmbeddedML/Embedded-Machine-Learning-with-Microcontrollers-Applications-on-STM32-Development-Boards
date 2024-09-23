import tensorflow as tf
import keras
from Common.tflite2cc import convert_tflite2cc

TFLITE_MODEL_PATH = "mlp_temperature_prediction.tflite"
mnist_rnn_model = keras.models.load_model("mlp_temperature_prediction.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(mnist_rnn_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS]
kws_rnn_lite = converter.convert()

with open(TFLITE_MODEL_PATH, "wb") as tflite_file:
    tflite_file.write(kws_rnn_lite)

convert_tflite2cc(TFLITE_MODEL_PATH, "mnist_rnn_model.")
