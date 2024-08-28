import os
from sklearn2c import SVMClassifier

dirname = os.path.dirname

model_path = os.path.join(dirname(__file__), "classification_models","svm_classifier.joblib")
export_path = os.path.join(dirname(__file__), "exported_models","svm_cls_config")

svm = SVMClassifier.load(model_path)
svm.export(export_path)
