import tensorflow as tf
import keras
from tflite2cc import convert_tflite2cc

TFLITE_MODEL_PATH = "mnist_cnn_model.tflite"
mnist_cnn_model = keras.models.load_model("mnist_cnn_model.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(mnist_cnn_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
mnist_cnn_lite = converter.convert()

with open(TFLITE_MODEL_PATH, "wb") as tflite_file:
    tflite_file.write(mnist_cnn_lite)

convert_tflite2cc(TFLITE_MODEL_PATH, "mnist_cnn_model")