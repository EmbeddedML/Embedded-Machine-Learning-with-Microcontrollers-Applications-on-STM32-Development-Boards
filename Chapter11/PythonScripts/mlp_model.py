import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng


size=1000

rng = default_rng()
noise = .1*rng.standard_normal(size)

x = np.linspace(0., 4*np.pi, size)
y = np.sin(x) + noise

"""
len=200
x = np.array(range(len))/len*10
noise = np.random.normal(0, .2, len)
y=np.sin(np.pi/2*x)+noise
"""

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(10, input_shape=[1], activation='sigmoid'),
  tf.keras.layers.Dense(10, activation='sigmoid'),
  tf.keras.layers.Dense(1, activation = 'linear')
  ])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.SGD(0.1))
model.fit(x, y, epochs=500, verbose=False)

yp = model.predict(x)

plt.plot(x,y,'r.')
plt.plot(x,yp,'b')

plt.show()