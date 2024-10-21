import numpy as np
import tensorflow as tf

x = tf.Variable(-3.0)
y = tf.Variable(3.0)
iters = 20
step = 0.1

xval, yval = np.meshgrid(np.arange(-3, 3, 0.1),np.arange(-3, 3, 0.1))
Z = xval * xval + yval * yval

for iter in range(iters):
    with tf.GradientTape() as tape:
        z = x * x + y * y
    x_before = tf.constant(x)
    y_before = tf.constant(y)
    dz = tape.gradient(z, [x,y])
    dx = -step * dz[0]
    dy = -step * dz[1]
    x.assign_add(dx)
    y.assign_add(dy)
    new_z = x*x + y*y
    print(f'x = {x.numpy():.2f}, y= {y.numpy():.2f}, z = {new_z.numpy():.2f}')