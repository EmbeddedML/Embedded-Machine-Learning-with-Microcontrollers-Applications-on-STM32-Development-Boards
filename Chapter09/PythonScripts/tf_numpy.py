import tensorflow as tf

T = tf.constant([[1,2,3],[4,5,6]])

print("Tensor T is ", T)

numpy_arr = T.numpy()
print("Numpy ndarray num_T value is ", numpy_arr)

N= tf.convert_to_tensor(numpy_arr)

print("Convert back to TF Tensor: ", N)