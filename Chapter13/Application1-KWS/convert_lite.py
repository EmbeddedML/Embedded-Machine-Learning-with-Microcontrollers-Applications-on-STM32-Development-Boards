import os
import tensorflow as tf
import keras
from Common.tflite2cc import convert_tflite2cc
from .data_loader import create_datasets
from Models.paths import TFLITE_MODEL_DIR, TFLITE_EXPORT_DIR, KERAS_MODEL_DIR

model_path = os.path.join(KERAS_MODEL_DIR, "kws_cnn.h5")
tflite_model_path = os.path.join(TFLITE_MODEL_DIR, "kws_cnn.tflite")
tflite_export_path = os.path.join(TFLITE_EXPORT_DIR, "kws_cnn")

kws_cnn_model = keras.models.load_model(model_path)
train_ds, *_ = create_datasets(8000, 512, 256, 32)
def representative_dataset():
    for input_value in train_ds.take(100):
        yield [input_value[0]]

converter = tf.lite.TFLiteConverter.from_keras_model(kws_cnn_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8  # or tf.uint8
converter.inference_output_type = tf.int8  # or tf.uint8
kws_cnn_lite = converter.convert()

with open(tflite_model_path, "wb") as tflite_file:
    tflite_file.write(kws_cnn_lite)

convert_tflite2cc(kws_cnn_lite, tflite_export_path)
