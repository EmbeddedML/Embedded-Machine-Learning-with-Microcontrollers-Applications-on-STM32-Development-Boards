import os.path as osp
from sklearn2c import KNNRegressor

model_path = osp.join("regression_models","knn_sine_reg.joblib")
export_path = osp.join("exported_models","regression","knn_config")

knn = KNNRegressor.load(model_path)
knn.export(export_path)