import os 
import tensorflow as tf
import keras
from Common.tflite2cc import convert_tflite2cc
from Models.paths import KERAS_MODEL_DIR, TFLITE_MODEL_DIR, TFLITE_EXPORT_DIR

model_path = os.path.join(KERAS_MODEL_DIR, "hdr_cnn.h5")
tflite_model_path = os.path.join(TFLITE_MODEL_DIR, "hdr_cnn.tflite")
tflite_export_path = os.path.join(TFLITE_EXPORT_DIR, "hdr_cnn")

(train_images, train_labels), (val_images, val_labels)  = keras.datasets.mnist.load_data()
data_shape = (32, 32, 3)

def prepare_tensor(images, out_shape):
    images = tf.expand_dims(images, axis=-1)
    images = tf.repeat(images, 3, axis=-1)
    images = tf.image.resize(images, out_shape[:2])
    images = images / 255.0
    return images

train_images = prepare_tensor(train_images, data_shape)

def representative_dataset():
    for i in range(0, 1000, 32):
        yield [train_images[i: i+32]]


hdr_cnn_model = keras.models.load_model(model_path)
converter = tf.lite.TFLiteConverter.from_keras_model(hdr_cnn_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.representative_dataset = representative_dataset
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8
hdr_cnn_lite = converter.convert()

with open(tflite_model_path, "wb") as tflite_file:
    tflite_file.write(hdr_cnn_lite)

convert_tflite2cc(hdr_cnn_lite, tflite_export_path)