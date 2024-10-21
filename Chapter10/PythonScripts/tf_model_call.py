import tensorflow as tf

class Model(tf.Module):
  def __init__(self):
    self.W = tf.Variable(1.0)
    self.b = tf.Variable(1.0)

  def __call__(self, x):
    self.out= tf.keras.activations.sigmoid(self.W * x + self.b)
    return self.out

model = Model()
u=model(0.0).numpy()

print(u)
