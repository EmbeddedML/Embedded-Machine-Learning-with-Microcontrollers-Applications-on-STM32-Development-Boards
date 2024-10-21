import os
from sklearn2c import DTClassifier
from Models.paths import CLASSIFICATION_MODEL_DIR, CLASSIFICATION_EXPORT_DIR

model_path = os.path.join(CLASSIFICATION_MODEL_DIR,"dt_classifier.joblib")
export_path = os.path.join(CLASSIFICATION_EXPORT_DIR,"dt_cls_config")

dtc = DTClassifier.load(model_path)
dtc.export(export_path)