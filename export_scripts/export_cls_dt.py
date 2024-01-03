import os.path as osp
from sklearn2c import DTClassifier

dtc = DTClassifier()
model_path = osp.join("classification_models","DTC_classifier.joblib")
export_path = osp.join("exported_models","classification","dtc_config")
dtc.load(model_path)
dtc.export(export_path)