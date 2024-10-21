import os
import numpy as np
from sklearn2c import LinearRegressor
from Data.paths import REGRESSION_DATA_DIR
from Models.paths import REGRESSION_MODEL_DIR

train_samples = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_samples.npy"))
train_line_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_line_values.npy"))
train_sine_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_sine_values.npy"))

line_linear_model = LinearRegressor()
linear_save_path = os.path.join(REGRESSION_MODEL_DIR,"linear_regressor_line.joblib")
line_linear_model.train(train_samples, train_line_values, linear_save_path)

sine_linear_model = LinearRegressor()
linear_save_path = os.path.join(REGRESSION_MODEL_DIR,"linear_regressor_sine.joblib")
sine_linear_model.train(train_samples, train_sine_values, linear_save_path)