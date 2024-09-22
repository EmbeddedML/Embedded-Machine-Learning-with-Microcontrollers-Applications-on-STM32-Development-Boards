import os
import numpy as np
from sklearn2c import BayesClassifier
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import CLASSIFICATION_MODEL_DIR

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_labels.npy"))

bayesian = BayesClassifier(case=3)
model_save_path = os.path.join(CLASSIFICATION_MODEL_DIR, "bayes_classifier.joblib")
bayesian.train(train_samples, train_labels, save_path=model_save_path)
