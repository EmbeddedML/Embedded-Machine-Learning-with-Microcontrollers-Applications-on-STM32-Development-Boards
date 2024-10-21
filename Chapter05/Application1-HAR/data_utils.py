import pandas as pd

def read_data(file_path):
    column_names = ["user", "activity", "timestamp", "x-accel", "y-accel", "z-accel"]
    df = pd.read_csv(file_path, header=None, names=column_names)
    df["z-accel"] = df["z-accel"].str.replace(";", "").astype(float)
    df.dropna(inplace=True)
    print(f"Number of columns in the dataframe: {df.shape[1]}")
    print(f"Number of rows in the dataframe: {df.shape[0]}")
    df.head()
    return df