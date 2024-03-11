import os.path as osp
from sklearn2c import BayesClassifier

model_path = osp.join("classification_models", "bayes_classifier.joblib")
export_path = osp.join("exported_models", "classification", "bayes_cls_config")

bayesian = BayesClassifier.load(model_path)
bayesian.export(export_path)