import os
from .data_utils import read_data
from .feature_utils import create_features
from Data.paths import WISDM_PATH

TIME_PERIODS = 80
STEP_DISTANCE = 40
data_df = read_data(WISDM_PATH)
df_train = data_df[data_df["user"] <= 28]
df_test = data_df[data_df["user"] > 28]

train_segments_df, train_labels = create_features(df_train, TIME_PERIODS, STEP_DISTANCE)
test_segments_df, test_labels = create_features(df_test, TIME_PERIODS, STEP_DISTANCE)

print("Train samples shape: ", len(train_segments_df))
print("Train labels shape: ", train_labels.shape)
print("Test samples shape: ", len(test_segments_df))
print("Test labels shape: ", test_labels.shape)