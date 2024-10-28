import os
from .data_utils import read_data
from .feature_utils import create_features
from sklearn2c import Dbscan
from Data.paths import WISDM_PATH
from Models.paths import CLUSTERING_MODEL_DIR, CLUSTERING_EXPORT_DIR

TIME_PERIODS = 80
STEP_DISTANCE = 40
data_df = read_data(WISDM_PATH)
df_train = data_df[data_df["user"] <= 28]
df_test = data_df[data_df["user"] > 28]

train_segments_df, train_labels = create_features(df_train, TIME_PERIODS, STEP_DISTANCE)
dbscan = Dbscan(eps = 8, min_samples = 5)
dbscan.train(train_segments_df, os.path.join(CLUSTERING_MODEL_DIR, "har_dbscan.joblib"))
dbscan.predict(train_segments_df)
dbscan.export(os.path.join(CLUSTERING_EXPORT_DIR,"har_dbscan"))
