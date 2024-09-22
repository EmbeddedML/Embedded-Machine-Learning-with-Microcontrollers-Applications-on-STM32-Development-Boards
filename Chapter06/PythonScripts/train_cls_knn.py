import os
import numpy as np
from sklearn2c import KNNClassifier
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import CLASSIFICATION_MODEL_DIR

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_labels.npy"))

knn = KNNClassifier(n_neighbors = 5)
model_save_path = os.path.join(CLASSIFICATION_MODEL_DIR, "knn_classifier.joblib")
knn.train(train_samples, train_labels, save_path=model_save_path)