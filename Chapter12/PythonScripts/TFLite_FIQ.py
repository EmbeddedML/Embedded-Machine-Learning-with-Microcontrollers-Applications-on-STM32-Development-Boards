import os
import numpy as np
import tensorflow as tf
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import SAVED_MODEL_DIR, TFLITE_MODEL_DIR

saved_model_dir = os.path.join(SAVED_MODEL_DIR, "nn_classification")
int_w_float_model_path = os.path.join(TFLITE_MODEL_DIR, "quantized_model_int_w_float.tflite")
full_int_model_path = os.path.join(TFLITE_MODEL_DIR, "quantized_model_full_int.tflite")

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))

# Convert train_samples to float32 format
train_samples = train_samples.astype(np.float32)


def representative_dataset():
    for input_value in (tf.data.Dataset.from_tensor_slices(train_samples).batch(1).take(100)):
        yield [input_value]


# Full integer quantization
# Integer with float fallback (using default float input/output)
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
tflite_model_quant = converter.convert()

# Save the model.
with open(int_w_float_model_path, "wb") as f:
    f.write(tflite_model_quant)

# Full integer quantization
# Integer only
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
# Ensure that if any ops can't be quantized, the converter throws an error
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
# Set the input and output tensors to int8
converter.inference_input_type = tf.uint8  # or tf.int8
converter.inference_output_type = tf.uint8  # or tf.int8
tflite_model_quant = converter.convert()

# Save the model.
with open(full_int_model_path, "wb") as f:
    f.write(tflite_model_quant)
