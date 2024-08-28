import os
import numpy as np
from sklearn2c import KNNClassifier

dirname = os.path.dirname

train_samples = np.load(os.path.join(dirname(__file__),"classification_data", "cls_train_samples.npy"))
train_labels = np.load(os.path.join(dirname(__file__),"classification_data", "cls_train_labels.npy"))

knn = KNNClassifier(n_neighbors = 5)
model_save_path = os.path.join(dirname(__file__), "classification_models", "knn_classifier.joblib")
knn.train(train_samples, train_labels, save_path=model_save_path)