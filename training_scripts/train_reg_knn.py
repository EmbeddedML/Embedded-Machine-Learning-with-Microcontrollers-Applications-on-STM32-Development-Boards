import os.path as osp
import numpy as np
from sklearn2c import KNNRegressor

train_samples = np.load(osp.join("regression_data", "reg_samples.npy"))
train_line_values = np.load(osp.join("regression_data", "reg_line_values.npy"))
train_sine_values = np.load(osp.join("regression_data", "reg_sine_values.npy"))

line_knn_model = KNNRegressor(n_neighbors = 5)
knn_save_path = osp.join("regression_models","knn_line_reg.joblib")
line_knn_model.train(train_samples, train_line_values, knn_save_path)

sine_knn_model = KNNRegressor(n_neighbors = 5)
knn_save_path = osp.join("regression_models","knn_sine_reg.joblib")
sine_knn_model.train(train_samples, train_sine_values, knn_save_path)