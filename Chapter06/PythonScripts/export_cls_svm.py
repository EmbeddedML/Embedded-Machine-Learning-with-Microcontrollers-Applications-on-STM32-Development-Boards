import os
from sklearn2c import SVMClassifier
from Models.paths import CLASSIFICATION_MODEL_DIR, CLASSIFICATION_EXPORT_DIR

model_path = os.path.join(CLASSIFICATION_MODEL_DIR,"svm_classifier.joblib")
export_path = os.path.join(CLASSIFICATION_EXPORT_DIR,"svm_cls_config")

svm = SVMClassifier.load(model_path)
svm.export(export_path)
