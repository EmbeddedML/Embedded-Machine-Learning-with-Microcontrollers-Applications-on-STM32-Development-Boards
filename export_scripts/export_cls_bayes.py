import os.path as osp
from sklearn2c import BayesClassifier

bayesian = BayesClassifier(case = 3)
model_path = osp.join("classification_models","bayes_classifier.joblib")
export_path = osp.join("exported_models","classification","bayes_config")
bayesian.load(model_path)
bayesian.export(export_path)