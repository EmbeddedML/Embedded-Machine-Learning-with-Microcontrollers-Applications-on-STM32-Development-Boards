import os
import numpy as np
import tensorflow as tf
import tensorflow_model_optimization as tfmot
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import SAVED_MODEL_DIR, TFLITE_MODEL_DIR

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_labels.npy"))
test_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_test_samples.npy"))
test_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_test_labels.npy"))

saved_model_path = os.path.join(SAVED_MODEL_DIR, "nn_classification")
qat_tflite_path = os.path.join(TFLITE_MODEL_DIR, "quantized_model_w_QAT.tflite")

model = tf.keras.models.load_model(saved_model_path)
model.summary()

# q_aware stands for for quantization aware.
q_aware_model = tfmot.quantization.keras.quantize_model(model)
# `quantize_model` requires a recompile.
q_aware_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
    loss=tf.keras.losses.BinaryCrossentropy(),
    metrics=[tf.keras.metrics.BinaryAccuracy(), tf.keras.metrics.FalseNegatives()],
)

q_aware_model.summary()

train_samples_subset = train_samples[0:100]  # out of 1000
train_labels_subset = train_labels[0:100]

q_aware_model.fit(
    train_samples_subset,
    train_labels_subset,
    batch_size=500,
    epochs=1,
    validation_split=0.1,
)

baseline_model_accuracy = model.evaluate(test_samples, test_labels, verbose=0)
q_aware_model_accuracy = q_aware_model.evaluate(test_samples, test_labels, verbose=0)

print("Baseline test accuracy:", baseline_model_accuracy)
print("Quant test accuracy:", q_aware_model_accuracy)

converter = tf.lite.TFLiteConverter.from_keras_model(q_aware_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model_quant = converter.convert()

# Save the model.
with open(qat_tflite_path, "wb") as f:
    f.write(tflite_model_quant)
