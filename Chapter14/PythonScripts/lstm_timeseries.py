import tensorflow as tf
import os
import numpy as np
from matplotlib import pyplot as plt
from Data.paths import REGRESSION_DATA_DIR

samples = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_samples.npy"))
line_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_line_values.npy"))
sine_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_sine_values.npy"))

series=sine_values

print(samples.shape)

plt.figure()
plt.plot(samples,series)

n_input = 1
time_length=9

ls=len(samples)

dataset=tf.keras.utils.timeseries_dataset_from_array(
    samples[:-1], 
    np.roll(series, -n_input)[:-1], 
    sequence_length=n_input,
    batch_size=time_length,
    end_index=ls-(ls-ls//time_length*time_length),
)

x_train=[]; y_train=[]
for inputs, targets in dataset:
  x_train.append(inputs.numpy())
  y_train.append(targets.numpy())

x_train = np.array(x_train) 
y_train = np.array(y_train)

print(x_train.shape, y_train.shape)

units=10

model = tf.keras.Sequential([
  tf.keras.layers.Input(shape=(time_length,n_input)),  
#  tf.keras.layers.SimpleRNN(units, unroll=True),
#  tf.keras.layers.GRU(units,unroll=True),
#  tf.keras.layers.LSTM(units,unroll=True),
  tf.keras.layers.LSTM(units),  
  tf.keras.layers.Dense(1)
])

model.compile(
  loss=tf.keras.losses.MeanSquaredError(), 
  optimizer=tf.keras.optimizers.Adam(1e-3))

history=model.fit(x_train,y_train, epochs=500, verbose=False)

model.summary()

plt.figure()
plt.xlabel('Epoch Number')
plt.ylabel("Loss")
plt.plot(history.history['loss'])

MODEL_NAME = 'LSTM'
MODEL_DIR = 'models'

model.save(os.path.join(MODEL_DIR, MODEL_NAME + '_model_tf'), save_format = "tf")
model.save(os.path.join(MODEL_DIR, MODEL_NAME + 'model_keras.h5'), save_format = "h5")

y_pred = model.predict(x_train)

x_t=x_train[:,0,:,:]
x_t = x_t.reshape(-1)

plt.figure()
plt.plot(samples,series)
plt.plot(x_t,y_pred,'r')
plt.show()

"""
# Prediction
# Bakilacak

dummy = np.arange(0, 20, 0.05)

testset=tf.keras.utils.timeseries_dataset_from_array(
    dummy[:-1], 
    np.roll(dummy, -n_input)[:-1], 
    sequence_length=n_input,
    batch_size=time_length,
)

x_test=[]
for inputs, targets in testset:
  x_test.append(inputs.numpy())

x_test = np.array(x_test) 

y_pred = model.predict(x_test)

x_t=x_test[:,0,:,:]
x_t = x_t.reshape(-1)

plt.figure()
plt.plot(samples,series)
plt.plot(x_t,y_pred,'r')
plt.show()
"""