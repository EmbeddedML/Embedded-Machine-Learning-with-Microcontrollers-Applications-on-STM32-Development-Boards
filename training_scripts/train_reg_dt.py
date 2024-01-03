import os.path as osp
import numpy as np
from sklearn2c import DTRegressor

train_samples = np.load(osp.join("regression_data", "reg_samples.npy"))
train_line_values = np.load(osp.join("regression_data", "reg_line_values.npy"))
train_sine_values = np.load(osp.join("regression_data", "reg_sine_values.npy"))

line_dtr_model = DTRegressor()
dtr_save_path = osp.join("regression_models", "dtr_line_reg.joblib")
line_dtr_model.train(train_samples, train_line_values, dtr_save_path)

sine_dtr_model = DTRegressor()
dtr_save_path = osp.join("regression_models", "dtr_sine_reg.joblib")
sine_dtr_model.train(train_samples, train_sine_values, dtr_save_path)
