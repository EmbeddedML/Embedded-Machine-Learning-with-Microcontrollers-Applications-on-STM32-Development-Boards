import os.path as osp
import numpy as np
import tensorflow as tf

DATA_DIR = "classification_data"
MODEL_DIR = "models"

train_samples = np.load(osp.join(DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(osp.join(DATA_DIR, "cls_train_labels.npy"))
test_samples = np.load(osp.join(DATA_DIR, "cls_test_samples.npy"))
test_labels = np.load(osp.join(DATA_DIR, "cls_test_labels.npy"))

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(20, input_shape=[2], activation='relu'),
  tf.keras.layers.Dense(1, activation = 'sigmoid')
  ])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(),
                       tf.keras.metrics.FalseNegatives()])
  

model.fit(train_samples, train_labels, validation_data = (test_samples, test_labels), epochs=50, verbose=1)
print("Finished training the model")

model.save(osp.join(MODEL_DIR,"nn_classification_model_tf"), save_format = "tf")
model.save(osp.join(MODEL_DIR, "nn_classification_model_keras.h5"), save_format = "h5")
model.evaluate(test_samples, test_labels)