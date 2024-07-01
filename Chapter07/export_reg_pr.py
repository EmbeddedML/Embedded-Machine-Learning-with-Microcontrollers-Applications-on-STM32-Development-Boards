import os.path as osp
from sklearn2c import PolynomialRegressor

# CHOOSE ONE OF THE MODELS
# Parameter poly_reg_config MUST NOT BE CHANGED 
# SINCE IT IS INCLUDED IN C INFERENCE FILES

#line_model_path = osp.join("regression_models","poly_regressor_line.joblib")
sine_model_path = osp.join("regression_models","poly_regressor_sine.joblib")

export_path = osp.join("exported_models","regression","poly_reg_config")

#poly_regressor = PolynomialRegressor.load(line_model_path)
poly_regressor = PolynomialRegressor.load(sine_model_path)

poly_regressor.export(export_path)