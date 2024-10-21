import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

size=1000

rng = default_rng()
noise = .1*rng.standard_normal(size)

x = np.linspace(-2, 2, size)
y = 3*x + 2 + noise

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(1, input_shape=[1]),
  ])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.SGD(0.1))

model.fit(x, y, epochs=50, verbose=False)

yp = model.predict(x)

plt.plot(x,y,'r.')
plt.plot(x,yp,'b')
plt.show()