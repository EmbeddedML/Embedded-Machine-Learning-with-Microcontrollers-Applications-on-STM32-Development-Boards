import os.path as osp
import numpy as np
from sklearn2c import DTRegressor
from matplotlib import pyplot as plt

samples = np.load(osp.join("regression_data", "reg_samples.npy"))
line_values = np.load(osp.join("regression_data", "reg_line_values.npy"))
sine_values = np.load(osp.join("regression_data", "reg_sine_values.npy"))

line_model_path = osp.join("regression_models", "dt_regressor_line.joblib")
sine_model_path = osp.join("regression_models", "dt_regressor_sine.joblib")

dt_regressor_line = DTRegressor.load(line_model_path)
dt_regressor_sine = DTRegressor.load(sine_model_path)

line_predictions = dt_regressor_line.predict(samples)
sine_predictions = dt_regressor_sine.predict(samples)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(samples, line_values, "k.")
ax1.plot(samples, line_predictions, "b")
ax2.plot(samples, sine_values, "k.")
ax2.plot(samples, sine_predictions, "b")
plt.show()
