import os.path as osp
import numpy as np
from sklearn2c import BayesClassifier

train_samples = np.load(osp.join("classification_data", "cls_train_samples.npy"))
train_labels = np.load(osp.join("classification_data", "cls_train_labels.npy"))

bayesian = BayesClassifier(case=3)
model_save_path = osp.join("classification_models", "bayes_classifier.joblib")
bayesian.train(train_samples, train_labels, save_path=model_save_path)
