import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np

model = tf.keras.models.load_model('saved_model/my_model', compile=False)

model.summary()

# the data, split between train and test sets
(train_images, train_labels), (test_images, test_labels)  = tf.keras.datasets.mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

# Make sure images have shape (28, 28, 1)
train_images = np.expand_dims(train_images, -1)
test_images = np.expand_dims(test_images, -1)

test_ind=0
im = test_images[test_ind]

plt.figure()
plt.imshow(im, cmap = "gray")

img = np.expand_dims(im, 0)
layer = model.get_layer(name="conv2d")
feature_extractor = tf.keras.Model(inputs=model.inputs, outputs=layer.output)
activations = feature_extractor.predict(img) 
print(activations.shape)

filters, biases = layer.get_weights()

fig, ((conv_ax1, conv_ax2), (conv_ax3, conv_ax4)) = plt.subplots(2, 2)
ax = conv_ax1.imshow(filters[:, :, 0, 0], cmap = "gray")
ax = conv_ax2.imshow(filters[:, :, 0, 1], cmap = "gray")
ax = conv_ax3.imshow(filters[:, :, 0, 2], cmap = "gray")
ax = conv_ax4.imshow(filters[:, :, 0, 3], cmap = "gray")

fig, ((act_ax1, act_ax2), (act_ax3, act_ax4)) = plt.subplots(2, 2)
ax = act_ax1.imshow(activations[0, :, :, 0], cmap = "gray")
ax = act_ax2.imshow(activations[0, :, :, 1], cmap = "gray")
ax = act_ax3.imshow(activations[0, :, :, 2], cmap = "gray")
ax = act_ax4.imshow(activations[0, :, :, 3], cmap = "gray")

layer = model.get_layer(name="conv2d_1")
feature_extractor = tf.keras.Model(inputs=model.inputs, outputs=layer.output)
activations = feature_extractor.predict(img) 
print(activations.shape)

filters, biases = layer.get_weights()

fig, ((conv_ax1, conv_ax2), (conv_ax3, conv_ax4)) = plt.subplots(2, 2)
ax = conv_ax1.imshow(filters[:, :, 0, 0], cmap = "gray")
ax = conv_ax2.imshow(filters[:, :, 0, 1], cmap = "gray")
ax = conv_ax3.imshow(filters[:, :, 0, 2], cmap = "gray")
ax = conv_ax4.imshow(filters[:, :, 0, 3], cmap = "gray")

fig, ((act_ax1, act_ax2), (act_ax3, act_ax4)) = plt.subplots(2, 2)
ax = act_ax1.imshow(activations[0, :, :, 0], cmap = "gray")
ax = act_ax2.imshow(activations[0, :, :, 1], cmap = "gray")
ax = act_ax3.imshow(activations[0, :, :, 2], cmap = "gray")
ax = act_ax4.imshow(activations[0, :, :, 3], cmap = "gray")

plt.show()
