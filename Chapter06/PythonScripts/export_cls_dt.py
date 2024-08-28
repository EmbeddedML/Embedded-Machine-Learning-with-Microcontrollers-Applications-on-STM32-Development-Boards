import os
from sklearn2c import DTClassifier

dirname = os.path.dirname

model_path = os.path.join(dirname(__file__), "classification_models","dt_classifier.joblib")
export_path = os.path.join(dirname(__file__), "exported_models","dt_cls_config")

dtc = DTClassifier.load(model_path)
dtc.export(export_path)