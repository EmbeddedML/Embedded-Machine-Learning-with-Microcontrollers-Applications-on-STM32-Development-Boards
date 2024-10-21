import tensorflow as tf
import numpy as np

n_input = 1
n_units = 1

batch_size = 8; 
x=np.zeros((1, batch_size, n_input))
x[0,0,:]=1

# RNN layer definition
Wh = 1
init_Wh = tf.keras.initializers.constant(Wh)

Uh = 1
init_Uh = tf.keras.initializers.constant(Uh)

bh = -0.5
init_bh = tf.keras.initializers.constant(bh)

def hard_limiting(x):
    return tf.math.maximum(tf.math.sign(x),0)

rnn_layer=tf.keras.layers.SimpleRNN(
    units=n_units,
    bias_initializer=init_bh, 
    kernel_initializer=init_Wh, 
    recurrent_initializer=init_Uh, 
    activation=hard_limiting,
    return_sequences=True,
    return_state=True
    )

whole_sequence_output, final_state = rnn_layer(x)

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
out_conc=np.concatenate((x, whole_sequence_output.numpy()), axis=-1)
print("   Input, Output")
print(out_conc)
