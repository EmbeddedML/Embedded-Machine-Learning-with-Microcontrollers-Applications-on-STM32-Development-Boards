import tensorflow as tf
import numpy as np

n_input = 2
n_units = 2

batch_size = 10; 
x=np.zeros((1, batch_size, n_input))

x[0,0,:]=[1., 0.]
x[0,2,:]=[0., 1.]
x[0,3,:]=[0., 1.]
x[0,6,:]=[1., 0.]
x[0,7,:]=[1., 0.]

# RNN layer definition
Wh= np.array([[-1., 0.],
              [0., -1.]])
init_Wh = tf.keras.initializers.constant(Wh)

Uh= np.array([[0., -1.],
              [-1., 0.]])
init_Uh = tf.keras.initializers.constant(Uh)

bh = np.array([.5,.5])
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
    )

# Dense layer definition

Wy= np.array([[1],
              [0]],)
init_Wy = tf.keras.initializers.constant(Wy)

by = -0.5
init_by = tf.keras.initializers.constant(by)

dense_layer=tf.keras.layers.Dense(
    units=1, 
    kernel_initializer=init_Wy, 
    bias_initializer=init_by, 
    activation=hard_limiting,
    )

model = tf.keras.Sequential([
    rnn_layer,
    dense_layer
    ])

y = model(x)

model.summary()

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
out_conc=np.concatenate((x, y.numpy()), axis=-1)
print("   Input,       Output")
print(out_conc)