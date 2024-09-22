import numpy as np
import pandas as pd

def create_features(df, time_steps, step_size):
    x_segments = []
    y_segments = []
    z_segments = []
    labels = []
    for i in range(0, len(df) - time_steps, step_size):
        xs = df["x-accel"].values[i : i + time_steps]
        ys = df["y-accel"].values[i : i + time_steps]
        zs = df["z-accel"].values[i : i + time_steps]

        count_per_label = df["activity"][i : i + time_steps].value_counts()
        label_count = count_per_label.iloc[0]
        if label_count == time_steps:
            label = count_per_label.index[0]
            x_segments.append(xs)
            y_segments.append(ys)
            z_segments.append(zs)
            labels.append(label)

    # Bring the segments into a better shape
    segments_df = pd.DataFrame({"x_segments": x_segments,
                                "y_segments": y_segments,
                                "z_segments": z_segments}
    )
    feature_df = pd.DataFrame()
    # mean
    feature_df['x_mean'] = segments_df["x_segments"].apply(lambda x: x.mean())
    feature_df['y_mean'] = segments_df["y_segments"].apply(lambda x: x.mean())
    feature_df['z_mean'] = segments_df["z_segments"].apply(lambda x: x.mean())

    # positive count
    feature_df['x_pos_count'] = segments_df["x_segments"].apply(lambda x: np.sum(x > 0))
    feature_df['y_pos_count'] = segments_df["y_segments"].apply(lambda x: np.sum(x > 0))
    feature_df['z_pos_count'] = segments_df["z_segments"].apply(lambda x: np.sum(x > 0))

    # converting the signals from time domain to frequency domain using FFT
    FFT_SIZE = time_steps // 2 + 1
    x_fft_series = segments_df["x_segments"].apply(lambda x: np.abs(np.fft.fft(x))[1:FFT_SIZE])
    y_fft_series = segments_df["y_segments"].apply(lambda x: np.abs(np.fft.fft(x))[1:FFT_SIZE])
    z_fft_series = segments_df["z_segments"].apply(lambda x: np.abs(np.fft.fft(x))[1:FFT_SIZE])

    # FFT std dev
    feature_df['x_std_fft'] = x_fft_series.apply(lambda x: x.std())
    feature_df['y_std_fft'] = y_fft_series.apply(lambda x: x.std())
    feature_df['z_std_fft'] = z_fft_series.apply(lambda x: x.std())

    # FFT Signal magnitude area
    feature_df['sma_fft'] = x_fft_series.apply(lambda x: np.sum(abs(x)/50)) + y_fft_series.apply(lambda x: np.sum(abs(x)/50)) \
                        + z_fft_series.apply(lambda x: np.sum(abs(x)/50))


    labels = np.asarray(labels)

    return feature_df, labels