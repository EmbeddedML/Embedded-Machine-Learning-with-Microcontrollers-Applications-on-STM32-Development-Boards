import tensorflow as tf

a = tf.Variable([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
b = tf.Variable([[4, 5, 6], [5, 6, 7], [6, 7, 8]])

add1 = tf.add(a, b)
add2 = a + b

print("Addition with the add function: ", add1)
print("Addition with the + operator: ", add2)

sub1 = tf.subtract(a, b)
sub2 = a - b

print("Subtraction with the subtract function: ", sub1)
print("Subtraction with the - operator: ", sub2)
