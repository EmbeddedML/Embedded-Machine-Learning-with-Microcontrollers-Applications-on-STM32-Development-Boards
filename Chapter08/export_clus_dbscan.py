import os.path as osp
from sklearn2c.clustering import Dbscan

dbscan_model_dir = osp.join("clustering_models", "dbscan_clustering.joblib")
dbscan_config_dir = osp.join("exported_models", "clustering", "dbscan_clus_config")

dbscan = Dbscan.load(dbscan_model_dir)
dbscan.export(dbscan_config_dir)