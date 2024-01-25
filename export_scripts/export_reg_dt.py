import os.path as osp
from sklearn2c import DTRegressor

model_path = osp.join("regression_models","dtr_line_reg.joblib")
export_path = osp.join("exported_models","regression","dtr_config")

dtr = DTRegressor.load(model_path)
dtr.export(export_path)