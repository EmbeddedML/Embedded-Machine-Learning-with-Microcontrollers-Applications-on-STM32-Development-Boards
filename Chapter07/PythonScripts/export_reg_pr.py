import os
from sklearn2c import PolynomialRegressor
from Models.paths import REGRESSION_MODEL_DIR, REGRESSION_EXPORT_DIR

# CHOOSE ONE OF THE MODELS
# Parameter poly_reg_config MUST NOT BE CHANGED 
# SINCE IT IS INCLUDED IN C INFERENCE FILES

#line_model_path = os.path.join("regression_models","poly_regressor_line.joblib")
sine_model_path = os.path.join(REGRESSION_MODEL_DIR,"poly_regressor_sine.joblib")

export_path = os.path.join(REGRESSION_EXPORT_DIR,"poly_reg_config")

#poly_regressor = PolynomialRegressor.load(line_model_path)
poly_regressor = PolynomialRegressor.load(sine_model_path)

poly_regressor.export(export_path)