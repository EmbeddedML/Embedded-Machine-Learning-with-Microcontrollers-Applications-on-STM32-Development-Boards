import os
from sklearn2c.clustering import Dbscan
from Models.paths import CLUSTERING_MODEL_DIR, CLUSTERING_EXPORT_DIR

dbscan_model_dir = os.path.join(CLUSTERING_MODEL_DIR, "dbscan_clustering.joblib")
dbscan_config_dir = os.path.join(CLUSTERING_EXPORT_DIR, "dbscan_clus_config")

dbscan = Dbscan.load(dbscan_model_dir)
dbscan.export(dbscan_config_dir)