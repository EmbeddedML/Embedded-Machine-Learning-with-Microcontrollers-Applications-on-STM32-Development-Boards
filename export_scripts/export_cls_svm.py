import os.path as osp
from sklearn2c import SVMClassifier

svm = SVMClassifier()
model_path = osp.join("classification_models","SVM_classifier.joblib")
export_path = osp.join("exported_models","classification","SVM_config")
svm.load(model_path)
svm.export(export_path)
