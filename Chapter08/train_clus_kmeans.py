import os.path as osp
import numpy as np
from sklearn2c.clustering import Kmeans

train_samples = np.load(osp.join("classification_data", "cls_train_samples.npy"))
train_labels = np.load(osp.join("classification_data", "cls_train_labels.npy"))

kmeans = Kmeans(random_state = 42, n_init="auto")
kmeans_model_dir = osp.join("clustering_models", "kmeans_clustering.joblib")
kmeans.train(train_samples, save_path=kmeans_model_dir)