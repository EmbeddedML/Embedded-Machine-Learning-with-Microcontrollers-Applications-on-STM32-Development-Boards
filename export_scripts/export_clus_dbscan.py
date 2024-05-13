import os.path as osp
from sklearn2c.clustering import Dbscan

MODELS_DIR = "clustering_models"
CONFIG_DIR = osp.join("exported_models", "clustering")

dbscan_model_dir = osp.join(MODELS_DIR, "dbscan_clustering.joblib")
dbscan_config_dir = osp.join(CONFIG_DIR, "dbscan_clus_config")
dbscan = Dbscan.load(dbscan_model_dir)
dbscan.export(dbscan_config_dir)