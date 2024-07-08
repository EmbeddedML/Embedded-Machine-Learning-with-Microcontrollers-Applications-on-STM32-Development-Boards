import tensorflow as tf

class Model(tf.Module):
    def __init__(self, **kwargs):
        self.w = tf.Variable(5.0)
        self.b = tf.Variable(0.0)

    def __call__(self, x):
        return self.w * x + self.b