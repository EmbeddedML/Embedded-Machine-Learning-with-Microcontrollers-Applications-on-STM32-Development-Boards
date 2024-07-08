import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import os.path as osp

num_classes = 10

# the data, split between train and test sets
(train_images, train_labels), (test_images, test_labels)  = tf.keras.datasets.mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

# Make sure images have shape (28, 28, 1)
train_images = np.expand_dims(train_images, -1)
test_images = np.expand_dims(test_images, -1)

print("train images shape:", train_images.shape)
print(train_images.shape[0], "train samples")
print(test_images.shape[0], "test samples")

units = 16

model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(28, 28)),  
#    tf.keras.layers.SimpleRNN(units, unroll=True),
#    tf.keras.layers.GRU(units,unroll=True),
    tf.keras.layers.LSTM(units,unroll=True),
    tf.keras.layers.Dense(num_classes, activation="softmax"),
])

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, batch_size=64, epochs=5, validation_split=0.1)

MODEL_NAME = 'LSTM'
MODEL_DIR = 'models'

model.save(osp.join(MODEL_DIR, MODEL_NAME + '_model_tf'), save_format = "tf")
model.save(osp.join(MODEL_DIR, MODEL_NAME + 'model_keras.h5'), save_format = "h5")