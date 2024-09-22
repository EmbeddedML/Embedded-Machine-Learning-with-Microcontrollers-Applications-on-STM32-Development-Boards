import numpy as np
import os 
from sklearn2c.clustering import Dbscan
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import CLUSTERING_MODEL_DIR

train_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_labels.npy"))

dbscan = Dbscan(eps = 1)
model_save_path = os.path.join(CLUSTERING_MODEL_DIR, "dbscan_clustering.joblib")
dbscan.train(train_samples, model_save_path)