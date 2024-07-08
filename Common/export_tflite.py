import tensorflow as tf
from tflite2cc import convert_tflite2cc

model = tf.keras.models.load_model("mlp_mnist_model.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
convert_tflite2cc(tflite_model, "mlp_mnist_model")