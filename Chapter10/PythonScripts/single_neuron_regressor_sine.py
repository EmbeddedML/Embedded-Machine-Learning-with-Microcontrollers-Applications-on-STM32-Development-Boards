import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # For reproducibility
size=200

x = np.array(range(size))/size*10

noise = np.random.normal(0, .5, size)
y1=3*x+4+noise

noise = np.random.normal(0, .2, size)
y2=np.sin(np.pi/2*x)+noise

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(1, input_shape=[1]),
  ])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.SGD(0.001))
model.fit(x, y1, epochs=100)
y1_pred = model.predict(x)

model.fit(x, y2, epochs=100)
y2_pred = model.predict(x)


plt.figure(1)
plt.scatter(x, y1, c = 'k')
plt.plot(x, y1_pred, 'b')

plt.figure(2)
plt.scatter(x ,y2, c = 'k')
plt.plot(x, y2_pred, 'b')
plt.show()