import os.path as osp
from sklearn2c import KNNRegressor

# CHOOSE ONE OF THE MODELS
# Parameter knn_reg_config MUST NOT BE CHANGED 
# SINCE IT IS INCLUDED IN C INFERENCE FILES

#line_model_path = osp.join("regression_models","knn_regressor_line.joblib")
sine_model_path = osp.join("regression_models","knn_regressor_sine.joblib")

export_path = osp.join("exported_models","regression","knn_reg_config")

#knn_regressor = KNNRegressor.load(line_model_path)
knn_regressor = KNNRegressor.load(sine_model_path)

knn_regressor.export(export_path)