import os.path as osp
from sklearn2c import DTClassifier

model_path = osp.join("classification_models","dt_classifier.joblib")
export_path = osp.join("exported_models","classification","dt_cls_config")

dtc = DTClassifier.load(model_path)
dtc.export(export_path)