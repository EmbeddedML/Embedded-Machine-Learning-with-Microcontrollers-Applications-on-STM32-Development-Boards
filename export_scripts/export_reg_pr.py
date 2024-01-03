import os.path as osp
from sklearn2c import PolynomialRegressor

poly = PolynomialRegressor(3)
model_path = osp.join("regression_models", "poly_sine_reg.joblib")
export_path = osp.join("exported_models", "regression", "poly_reg_config")
poly.load(model_path)
poly.export(export_path)
