import os.path as osp
import numpy as np
from sklearn2c import PolynomialRegressor

train_samples = np.load(osp.join("regression_data", "reg_samples.npy"))
train_line_values = np.load(osp.join("regression_data", "reg_line_values.npy"))
train_sine_values = np.load(osp.join("regression_data", "reg_sine_values.npy"))

line_poly_model = PolynomialRegressor(deg = 6)
poly_save_path = osp.join("regression_models","poly_regressor_line.joblib")
line_poly_model.train(train_samples, train_line_values, poly_save_path)

sine_poly_model = PolynomialRegressor(deg = 6)
poly_save_path = osp.join("regression_models","poly_regressor_sine.joblib")
sine_poly_model.train(train_samples, train_sine_values, poly_save_path)