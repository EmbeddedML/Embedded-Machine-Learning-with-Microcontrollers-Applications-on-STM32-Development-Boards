import os.path as osp
from sklearn2c import LinearRegressor

model_path = osp.join("regression_models","linear_regressor_sine.joblib")
export_path = osp.join("exported_models","regression","linear_reg_config")
linear = LinearRegressor.load(model_path)
linear.export(export_path)
