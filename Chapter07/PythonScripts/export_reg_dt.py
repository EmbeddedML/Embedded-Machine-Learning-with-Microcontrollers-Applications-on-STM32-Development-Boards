import os
from sklearn2c import DTRegressor
from Models.paths import REGRESSION_MODEL_DIR, REGRESSION_EXPORT_DIR

# CHOOSE ONE OF THE MODELS
# Parameter dt_reg_config MUST NOT BE CHANGED 
# SINCE IT IS INCLUDED IN C INFERENCE FILES

#line_model_path = os.path.join("regression_models","dt_regressor_line.joblib")
sine_model_path = os.path.join(REGRESSION_MODEL_DIR,"dt_regressor_sine.joblib")

export_path = os.path.join(REGRESSION_EXPORT_DIR,"dt_reg_config")

#dt_regressor = DTRegressor.load(line_model_path)
dt_regressor = DTRegressor.load(sine_model_path)

dt_regressor.export(export_path)