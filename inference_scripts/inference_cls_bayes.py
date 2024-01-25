import os.path as osp
import numpy as np
from sklearn2c import BayesClassifier

test_samples = np.load(osp.join("classification_data","cls_test_samples.npy"))
test_labels = np.load(osp.join("classification_data","cls_test_labels.npy"))

bayesian = BayesClassifier.load(osp.join("classification_models", "bayes_classifier.joblib"))
likelihood = bayesian.inference(test_samples)
print(likelihood)