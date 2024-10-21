import os
from sklearn2c import KNNClassifier
from Models.paths import CLASSIFICATION_MODEL_DIR, CLASSIFICATION_EXPORT_DIR

model_path = os.path.join(CLASSIFICATION_MODEL_DIR,"knn_classifier.joblib")
export_path = os.path.join(CLASSIFICATION_EXPORT_DIR,"knn_cls_config")
knn = KNNClassifier.load(model_path)
knn.export(export_path)
