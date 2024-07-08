import os.path as osp
from sklearn2c import DTRegressor

# CHOOSE ONE OF THE MODELS
# Parameter dt_reg_config MUST NOT BE CHANGED 
# SINCE IT IS INCLUDED IN C INFERENCE FILES

#line_model_path = osp.join("regression_models","dt_regressor_line.joblib")
sine_model_path = osp.join("regression_models","dt_regressor_sine.joblib")

export_path = osp.join("exported_models","regression","dt_reg_config")

#dt_regressor = DTRegressor.load(line_model_path)
dt_regressor = DTRegressor.load(sine_model_path)

dt_regressor.export(export_path)