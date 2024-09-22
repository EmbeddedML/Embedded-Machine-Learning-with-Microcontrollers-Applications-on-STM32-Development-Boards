import os
import numpy as np
from sklearn2c import KNNRegressor
from Data.paths import REGRESSION_DATA_DIR
from Models.paths import REGRESSION_MODEL_DIR

train_samples = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_samples.npy"))
train_line_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_line_values.npy"))
train_sine_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_sine_values.npy"))

line_knn_model = KNNRegressor(n_neighbors = 5)
knn_save_path = os.path.join(REGRESSION_MODEL_DIR,"knn_regressor_line.joblib")
line_knn_model.train(train_samples, train_line_values, knn_save_path)

sine_knn_model = KNNRegressor(n_neighbors = 5)
knn_save_path = os.path.join(REGRESSION_MODEL_DIR,"knn_regressor_sine.joblib")
sine_knn_model.train(train_samples, train_sine_values, knn_save_path)