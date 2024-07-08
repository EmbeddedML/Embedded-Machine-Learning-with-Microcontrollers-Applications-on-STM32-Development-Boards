import os.path as osp
from sklearn2c.clustering import Kmeans

kmeans_model_dir = osp.join("clustering_models", "kmeans_clustering.joblib")
kmeans_config_dir = osp.join("exported_models", "clustering", "kmeans_clus_config")

kmeans = Kmeans.load(kmeans_model_dir)
kmeans.export(kmeans_config_dir)