import os.path as osp
from sklearn2c import KNNRegressor

# CHOOSE ONE OF THE MODELS
# Parameter knn_reg_config MUST NOT BE CHANGED 
# SINCE IT IS INCLUDED IN C INFERENCE FILES

#line_model_path = osp.join("regression_models","knn_regressor_line.joblib")
#line_export_path = osp.join("exported_models","regression","knn_reg_config")

sine_model_path = osp.join("regression_models","knn_regressor_sine.joblib")
sine_export_path = osp.join("exported_models","regression","knn_reg_config")

#line_knn = KNNRegressor.load(line_model_path)
#line_knn.export(line_export_path)

sine_knn = KNNRegressor.load(sine_model_path)
sine_knn.export(sine_export_path)