import os
import numpy as np
import tensorflow as tf
import keras
from Common.tflite2cc import convert_tflite2cc
from Models.paths import TFLITE_MODEL_DIR, TFLITE_EXPORT_DIR, KERAS_MODEL_DIR

model_path = os.path.join(KERAS_MODEL_DIR, "hdr_rnn.h5")
tflite_model_path = os.path.join(TFLITE_MODEL_DIR, "hdr_rnn.tflite")
tflite_export_path = os.path.join(TFLITE_EXPORT_DIR, "hdr_rnn")

(train_imgs, train_labels), _ = keras.datasets.mnist.load_data()
train_imgs = train_imgs.astype(np.float32) / 255.0

def representative_dataset():
    for i in range(0, 1000, 32):
        yield [train_imgs[i: i+32]]

hdr_rnn_model = keras.models.load_model(model_path)
converter = tf.lite.TFLiteConverter.from_keras_model(hdr_rnn_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.representative_dataset = representative_dataset
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8
hdr_rnn_lite = converter.convert()

with open(tflite_model_path, "wb") as tflite_file:
    tflite_file.write(hdr_rnn_lite)

convert_tflite2cc(hdr_rnn_lite, tflite_export_path)
