import tensorflow as tf
import os.path as osp
import numpy as np

samples = np.load(osp.join("regression_data", "reg_samples.npy"))
line_values = np.load(osp.join("regression_data", "reg_line_values.npy"))
sine_values = np.load(osp.join("regression_data", "reg_sine_values.npy"))

series=sine_values

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