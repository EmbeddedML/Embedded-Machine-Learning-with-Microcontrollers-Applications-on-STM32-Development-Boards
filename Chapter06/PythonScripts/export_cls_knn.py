import os
from sklearn2c import KNNClassifier

dirname = os.path.dirname

model_path = os.path.join(dirname(__file__),"classification_models","knn_classifier.joblib")
export_path = os.path.join(dirname(__file__), "exported_models","knn_cls_config")
knn = KNNClassifier.load(model_path)
knn.export(export_path)
