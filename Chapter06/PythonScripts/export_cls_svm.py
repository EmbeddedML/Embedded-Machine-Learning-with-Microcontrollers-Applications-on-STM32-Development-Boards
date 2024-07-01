import os.path as osp
from sklearn2c import SVMClassifier

model_path = osp.join("classification_models","svm_classifier.joblib")
export_path = osp.join("exported_models","classification","svm_cls_config")

svm = SVMClassifier.load(model_path)
svm.export(export_path)
