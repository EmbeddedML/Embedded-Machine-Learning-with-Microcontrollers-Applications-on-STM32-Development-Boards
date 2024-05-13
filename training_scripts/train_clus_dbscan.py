import os.path as osp
from sklearn.datasets import make_blobs
from sklearn2c.clustering import Dbscan
from sklearn.model_selection import train_test_split

samples, _ = make_blobs(200, 2, centers = 3, random_state= 42)
train_samples, test_samples = train_test_split(
    samples, test_size=0.2, random_state=42
)
MODELS_DIR = "clustering_models"

dbscan = Dbscan(eps = 1)
dbscan_model_dir = osp.join(MODELS_DIR, "dbscan_clustering.joblib")
dbscan.train(train_samples, save_path=dbscan_model_dir)
