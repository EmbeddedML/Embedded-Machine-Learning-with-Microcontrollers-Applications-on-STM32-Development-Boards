import os
import numpy as np
from sklearn2c.clustering import Kmeans
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import CLUSTERING_MODEL_DIR

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_labels.npy"))

kmeans = Kmeans(random_state = 42, n_init="auto")
kmeans_model_dir = os.path.join(CLUSTERING_MODEL_DIR, "kmeans_clustering.joblib")
kmeans.train(train_samples, save_path=kmeans_model_dir)