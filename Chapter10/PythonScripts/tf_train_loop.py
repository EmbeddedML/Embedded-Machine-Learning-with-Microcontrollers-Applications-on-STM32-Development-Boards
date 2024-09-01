import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

size=1000

rng = default_rng(0)
noise = .1*rng.standard_normal(size)

x = np.linspace(-2, 2, size)
y = 3*x + 2 + noise

class Model(tf.Module):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.w = tf.Variable(5.0)
    self.b = tf.Variable(0.0)

  def __call__(self, x):
    return self.w * x + self.b

model = Model()

# Compute a single loss value for an entire batch
def loss(target_y, predicted_y):
  return tf.reduce_mean(tf.square(target_y - predicted_y))

# Given a callable model, inputs, outputs, and a learning rate...
def train(model, x, y, learning_rate):

  with tf.GradientTape() as t:
    # Trainable variables are automatically tracked by GradientTape
    current_loss = loss(y, model(x))

  # Use GradientTape to calculate the gradients with respect to W and b
  dw, db = t.gradient(current_loss, [model.w, model.b])

  # Subtract the gradient scaled by the learning rate
  model.w.assign_sub(learning_rate * dw)
  model.b.assign_sub(learning_rate * db)

model = Model()

epochs = range(10)

def training_loop(model, x, y):
  for epoch in epochs:
    # Update the model with the single giant batch
    train(model, x, y, learning_rate=0.1)

# Do the training
training_loop(model, x, y)

yp = model(x)

plt.plot(x,y,'r.')
plt.plot(x,yp,'b')
plt.show()