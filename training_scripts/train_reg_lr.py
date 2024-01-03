import os.path as osp
import numpy as np
from sklearn2c import LinearRegressor


train_samples = np.load(osp.join("regression_data", "reg_samples.npy"))
train_line_values = np.load(osp.join("regression_data", "reg_line_values.npy"))
train_sine_values = np.load(osp.join("regression_data", "reg_sine_values.npy"))

line_linear_model = LinearRegressor()
linear_save_path = osp.join("regression_models","linear_line_reg.joblib")
line_linear_model.train(train_samples, train_line_values, linear_save_path)

sine_linear_model = LinearRegressor()
linear_save_path = osp.join("regression_models","linear_sine_reg.joblib")
sine_linear_model.train(train_samples, train_sine_values, linear_save_path)