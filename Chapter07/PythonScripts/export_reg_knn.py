import os
from sklearn2c import KNNRegressor
from Models.paths import REGRESSION_MODEL_DIR, REGRESSION_EXPORT_DIR

# CHOOSE ONE OF THE MODELS
# Parameter knn_reg_config MUST NOT BE CHANGED 
# SINCE IT IS INCLUDED IN C INFERENCE FILES

#line_model_path = os.path.join("regression_models","knn_regressor_line.joblib")
sine_model_path = os.path.join(REGRESSION_MODEL_DIR,"knn_regressor_sine.joblib")

export_path = os.path.join(REGRESSION_EXPORT_DIR,"knn_reg_config")

#knn_regressor = KNNRegressor.load(line_model_path)
knn_regressor = KNNRegressor.load(sine_model_path)

knn_regressor.export(export_path)