import os.path as osp
from sklearn2c import LinearRegressor

model_path = osp.join("regression_models","linear_sine_reg.joblib")
export_path = osp.join("exported_models","regression","lin_reg_config")
linear = LinearRegressor.load(model_path)
linear.export(export_path)
