import os
from sklearn2c.clustering import Kmeans
from Models.paths import CLUSTERING_MODEL_DIR, CLUSTERING_EXPORT_DIR

kmeans_model_dir = os.path.join(CLUSTERING_MODEL_DIR, "kmeans_clustering.joblib")
kmeans_config_dir = os.path.join(CLUSTERING_EXPORT_DIR, "kmeans_clus_config")

kmeans = Kmeans.load(kmeans_model_dir)
kmeans.export(kmeans_config_dir)