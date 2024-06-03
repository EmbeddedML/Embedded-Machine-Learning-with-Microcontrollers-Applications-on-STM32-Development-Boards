import numpy as np
import os.path as osp 
from sklearn2c.clustering import Dbscan

train_samples = np.load(osp.join("classification_data", "cls_train_samples.npy"))
train_labels = np.load(osp.join("classification_data", "cls_train_labels.npy"))

dbscan = Dbscan(eps = 1)
model_save_path = osp.join("clustering_models", "dbscan_clustering.joblib")
dbscan.train(train_samples, model_save_path)