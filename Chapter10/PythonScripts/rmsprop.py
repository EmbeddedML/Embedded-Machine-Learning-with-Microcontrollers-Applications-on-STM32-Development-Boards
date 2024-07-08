import tensorflow as tf

opt = tf.keras.optimizers.RMSprop(learning_rate=0.1)
var = tf.Variable(10.0)

loss = lambda: (var ** 2) / 2.0 

for _ in range(10):
    opt.minimize(loss, [var])
    print(var.numpy())