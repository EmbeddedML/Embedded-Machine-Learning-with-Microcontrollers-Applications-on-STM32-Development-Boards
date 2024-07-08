import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

im = Image.open('square1.jpg').convert('L')

plt.figure()
plt.imshow(im,cmap='gray')

# normalize to the range 0-1
im = np.asarray(im)
im=im/255.

img = np.expand_dims(im, 0)

sobel_x=np.array([[1, 0, -1],
                 [2, 0, -2],
                 [1, 0, -1]],dtype='float32')

sobel_y = sobel_x.T

filters=np.zeros([3,3,1,2])

filters[:,:,0,0]=sobel_x
filters[:,:,0,1]=sobel_y

init_kernel = tf.keras.initializers.constant(filters)

init_bias = np.zeros((2,))
init_bias = tf.keras.initializers.constant(init_bias)

conv_layer = tf.keras.layers.Conv2D(2, 
                                    kernel_size=(3, 3), 
                                    activation=None,
                                    kernel_initializer=init_kernel,
                                    bias_initializer=init_bias,
                                    padding='same',
                                    strides=[1, 1])

input_shape = (480, 640, 1)
model = tf.keras.Sequential([
        tf.keras.Input(shape=input_shape),
        conv_layer,
        ])

model.summary()

activations = model.predict(img) 
print(activations.shape)

layer = model.get_layer(name="conv2d")
weights, biases = layer.get_weights()

fig, (filter_ax1, filter_ax2) = plt.subplots(1, 2)
ax = filter_ax1.imshow(weights[:, :, 0, 0], cmap = 'gray')
ax=filter_ax2.imshow(weights[:, :, 0, 1], cmap = 'gray')

fig, (sobel_ax1, sobel_ax2) = plt.subplots(1, 2)
ax=sobel_ax1.imshow(activations[0, :, :, 0], cmap = 'gray')
ax=sobel_ax2.imshow(activations[0, :, :, 1], cmap = 'gray')

plt.show()
