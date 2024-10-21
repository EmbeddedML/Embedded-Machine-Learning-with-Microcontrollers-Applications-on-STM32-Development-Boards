import tensorflow as tf

a = tf.Variable([[1], [2]])
b = tf.Variable([[3, 4]])

vecmul = tf.matmul(a, b)

print("Vector multiplication: ", vecmul)

c = tf.Variable([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
d = tf.Variable([[4, 5, 6], [5, 6, 7], [6, 7, 8]])

matmul = tf.matmul(c, d)

print("Matrix multiplication: ", matmul)
