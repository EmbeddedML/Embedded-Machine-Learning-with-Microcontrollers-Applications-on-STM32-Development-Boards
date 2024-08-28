import os
from sklearn2c import BayesClassifier

dirname = os.path.dirname

model_path = os.path.join(dirname(__file__),"classification_models", "bayes_classifier.joblib")
export_path = os.path.join(dirname(__file__),"exported_models", "bayes_cls_config")

bayesian = BayesClassifier.load(model_path)
bayesian.export(export_path)