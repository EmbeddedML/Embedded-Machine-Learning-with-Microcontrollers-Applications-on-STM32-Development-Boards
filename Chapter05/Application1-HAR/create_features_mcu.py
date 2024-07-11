import numpy as np

def create_features(acc_input, time_steps):
    acc_input = acc_input.reshape(time_steps, 3, order = "F")
    features = []
    xs = acc_input[:,0]
    ys = acc_input[:,1]
    zs = acc_input[:,2]

    # mean
    x_mean = xs.mean()
    y_mean = ys.mean()
    z_mean = zs.mean()

    # positive count
    x_pos_count = np.sum(xs > 0)
    y_pos_count = np.sum(ys > 0)
    z_pos_count = np.sum(zs > 0)

    # converting the signals from time domain to frequency domain using FFT
    FFT_SIZE = time_steps // 2 + 1
    x_fft = np.abs(np.fft.fft(xs))[1:FFT_SIZE]
    y_fft = np.abs(np.fft.fft(ys))[1:FFT_SIZE]
    z_fft = np.abs(np.fft.fft(zs))[1:FFT_SIZE]

    # FFT std dev
    x_std_fft = x_fft.std()
    y_std_fft = y_fft.std()
    z_std_fft = z_fft.std()

    # FFT Signal magnitude area
    sma_fft = np.sum(abs(xs)/50) + np.sum(abs(ys)/50) + np.sum(abs(zs)/50)
    features = [x_mean, y_mean, z_mean, x_pos_count, y_pos_count, z_pos_count, x_std_fft, y_std_fft, z_std_fft, sma_fft]

    return features


if __name__ == "__main__":
    arr = np.arange(240)
    features = create_features(arr, 80)
    print(features)