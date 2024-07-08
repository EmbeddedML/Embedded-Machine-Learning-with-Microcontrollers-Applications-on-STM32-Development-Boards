import tensorflow as tf
from tflite2cc import convert_tflite2cc

model = tf.keras.models.load_model("mnist_single_neuron.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
convert_tflite2cc(tflite_model = tflite_model, cc_filename="mnist_single_neuron.cc")