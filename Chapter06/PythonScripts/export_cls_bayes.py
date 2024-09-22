import os
from sklearn2c import BayesClassifier
from Models.paths import CLASSIFICATION_MODEL_DIR, CLASSIFICATION_EXPORT_DIR

model_path = os.path.join(CLASSIFICATION_MODEL_DIR, "bayes_classifier.joblib")
export_path = os.path.join(CLASSIFICATION_EXPORT_DIR, "bayes_cls_config")

bayesian = BayesClassifier.load(model_path)
bayesian.export(export_path)