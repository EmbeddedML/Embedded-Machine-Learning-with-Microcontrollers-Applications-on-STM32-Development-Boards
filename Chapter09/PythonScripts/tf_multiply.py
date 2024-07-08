import tensorflow as tf

a = tf.Variable([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
b = tf.Variable([[4, 5, 6], [5, 6, 7], [6, 7, 8]])

mul1 = tf.multiply(a, b)
mul2 = a * b

print("Element-wise multiplication with the multiply function: ", mul1)
print("Element-wise multiplication with the * operator: ", mul2)
