import os
import numpy as np
from matplotlib import pyplot as plt
from sklearn2c import LinearRegressor
from Data.paths import REGRESSION_DATA_DIR
from Models.paths import REGRESSION_MODEL_DIR

samples = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_samples.npy"))
line_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_line_values.npy"))
sine_values = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_sine_values.npy"))

line_model_path = os.path.join(REGRESSION_MODEL_DIR, "linear_regressor_line.joblib")
sine_model_path = os.path.join(REGRESSION_MODEL_DIR, "linear_regressor_sine.joblib")

linear_regressor_line = LinearRegressor.load(line_model_path)
linear_regressor_sine = LinearRegressor.load(sine_model_path)

line_predictions = linear_regressor_line.predict(samples)
sine_predictions = linear_regressor_sine.predict(samples)

#Plotting functions
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(samples, line_values, "k.")
ax1.plot(samples, line_predictions, "b")
ax2.plot(samples, sine_values, "k.")
ax2.plot(samples, sine_predictions, "b")
plt.show()
