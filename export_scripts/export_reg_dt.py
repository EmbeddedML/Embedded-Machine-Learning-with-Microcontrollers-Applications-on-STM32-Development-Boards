import os.path as osp
from sklearn2c import DTRegressor

# CHOOSE ONE OF THE MODELS
# Parameter dt_reg_config MUST NOT BE CHANGED 
# SINCE IT IS INCLUDED IN C INFERENCE FILES

#line_model_path = osp.join("regression_models","dt_regressor_line.joblib")
#line_export_path = osp.join("exported_models","regression","dt_reg_config")

sine_model_path = osp.join("regression_models","dt_regressor_sine.joblib")
sine_export_path = osp.join("exported_models","regression","dt_reg_config")

#line_dt = DTRegressor.load(line_model_path)
#line_dt.export(line_export_path)

sine_dt = DTRegressor.load(sine_model_path)
sine_dt.export(sine_export_path)