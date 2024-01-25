import os.path as osp
import numpy as np
from sklearn2c import PolynomialRegressor
from matplotlib import pyplot as plt

samples = np.load(osp.join("regression_data", "reg_samples.npy"))
line_values = np.load(osp.join("regression_data", "reg_line_values.npy"))
sine_values = np.load(osp.join("regression_data", "reg_sine_values.npy"))

line_model_path = osp.join("regression_models","poly_line_reg.joblib")
sine_model_path = osp.join("regression_models","poly_sine_reg.joblib")
line_export_path = osp.join("exported_models","regression","lin_reg_config")

line_linear_model = PolynomialRegressor.load(line_model_path)
sine_linear_model = PolynomialRegressor.load(sine_model_path)

line_predictions = line_linear_model.inference(samples)
sine_predictions = sine_linear_model.inference(samples)

line_linear_model.export(line_export_path)

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(samples, line_values, "k.")
ax1.plot(samples, line_predictions, "b")
ax2.plot(samples, sine_values, "k.")
ax2.plot(samples, sine_predictions, "b")
plt.show()
