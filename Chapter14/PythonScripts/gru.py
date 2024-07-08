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

# GRU layer definition

Wz= np.array([[0., 0.],
              [0., 0.]])

Wr= np.array([[0., 0.],
              [0., 0.]])

Wh= np.array([[-1., 0.],
              [0., -1.]])

kernel_weights = np.concatenate((Wz, Wr, Wh), axis=1)
init_kw = tf.keras.initializers.constant(kernel_weights)

Uz= np.array([[0., 0.],
              [0., 0.]])

Ur= np.array([[0., 0.],
              [0., 0.]])

Uh= np.array([[0., -1.],
              [-1., 0.]])

recurrent_weights = np.concatenate((Uz, Ur, Uh), axis=1)
init_rw = tf.keras.initializers.constant(recurrent_weights)

bz=np.array([-.1, -.1]) 

br=np.array([.5, .5]) 

bh=np.array([.5, .5]) 

bias= np.concatenate((bz, br, bh), axis=0)
bias = tf.keras.initializers.constant(bias)

def hard_limiting(x):
    return tf.math.maximum(tf.math.sign(x),0)

GRU_layer=tf.keras.layers.GRU(
    units=n_units,
    use_bias=True,
    bias_initializer=bias, 
    kernel_initializer=init_kw, 
    recurrent_initializer=init_rw, 
    activation=hard_limiting,
    recurrent_activation=hard_limiting,
    reset_after=False,
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
    GRU_layer,
    dense_layer
    ])

y = model(x)

model.summary()

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
out_conc=np.concatenate((x, y.numpy()), axis=-1)
print("   Input,       Output")
print(out_conc)