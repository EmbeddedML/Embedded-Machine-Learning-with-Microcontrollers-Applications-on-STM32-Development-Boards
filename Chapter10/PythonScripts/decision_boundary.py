import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

w = tf.keras.initializers.Constant([.5, -0.5])
b = tf.keras.initializers.Constant(0.)
l0=tf.keras.layers.Dense(units=1, 
                         input_shape=[2], 
                         kernel_initializer=w, 
                         bias_initializer=b, 
                         activation='sigmoid')

model = tf.keras.Sequential([l0])

xval, yval = np.meshgrid(np.arange(-5, 5, 0.1),np.arange(-5, 5, 0.1))

Z = model.predict(np.c_[xval.ravel(), yval.ravel()])

Z = Z.reshape(xval.shape)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(xval, yval, Z, cmap=cm.coolwarm)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
