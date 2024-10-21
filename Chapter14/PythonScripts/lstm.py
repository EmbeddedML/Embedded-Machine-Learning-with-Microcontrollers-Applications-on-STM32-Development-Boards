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

# LSTM layer definition

Wi= np.array([[-1., 0.],
              [0., -1.]])

Wf= np.array([[0., 0.],
              [0., 0.]])

Wc= np.array([[0., 0.],
              [0., 0.]])

Wo= np.array([[0., 0.],
              [0., 0.]])


kernel_weights = np.concatenate((Wi, Wf, Wc, Wo), axis=1)
init_kw = tf.keras.initializers.constant(kernel_weights)


Ui= np.array([[0., -1.],
              [-1., 0.]])

Uf= np.array([[0., 0.],
              [0., 0.]])

Uc= np.array([[0., 0.],
              [0., 0.]])

Uo= np.array([[0., 0.],
              [0., 0.]])

recurrent_weights = np.concatenate((Ui, Uf, Uc, Uo), axis=1)
init_rw = tf.keras.initializers.constant(recurrent_weights)

bi=np.array([.5, .5]) 
bf=np.array([-.1, -.1]) 
bc=np.array([.5, .5]) 
bo=np.array([.1, .1]) 

bias= np.concatenate((bi, bf, bc, bo), axis=0)
bias = tf.keras.initializers.constant(bias)


def hard_limiting(x):
    return tf.math.maximum(tf.math.sign(x),0)

LSTM_layer=tf.keras.layers.LSTM(
    units=n_units,
    use_bias=True,
    bias_initializer=bias, 
    unit_forget_bias=False,
    kernel_initializer=init_kw, 
    recurrent_initializer=init_rw, 
    activation=hard_limiting,
    recurrent_activation=hard_limiting,
    return_sequences=True, 
    )

# Dense layer definition

Wy= np.array([[1.],
              [0.]],)
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
    LSTM_layer,
    dense_layer
    ])

y = model(x)

model.summary()

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
out_conc=np.concatenate((x, y.numpy()), axis=-1)
print("   Input,       Output")
print(out_conc)
