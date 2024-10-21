import tensorflow as tf
import os
import numpy as np
from Data.paths import REGRESSION_DATA_DIR

samples = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_samples.npy"))
line_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_line_values.npy"))
sine_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_sine_values.npy"))

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