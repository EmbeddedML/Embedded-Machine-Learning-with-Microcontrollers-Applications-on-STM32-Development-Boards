import os
import numpy as np
from sklearn2c import BayesClassifier

dirname = os.path.dirname

test_samples = np.load(os.path.join(dirname(__file__),"classification_data","cls_test_samples.npy"))
test_labels = np.load(os.path.join(dirname(__file__),"classification_data","cls_test_labels.npy"))

bayesian = BayesClassifier.load(os.path.join(dirname(__file__), "classification_models", "bayes_classifier.joblib"))
likelihood = bayesian.predict(test_samples)
print(likelihood)