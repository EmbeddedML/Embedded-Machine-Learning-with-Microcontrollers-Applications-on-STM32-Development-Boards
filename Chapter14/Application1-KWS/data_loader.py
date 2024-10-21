import os
import tensorflow as tf
from Data.paths import FSDD_PATH

def mel_spectrogram(wav_path, params):
    sample_len = params[0]
    fft_len = params[1]
    step = params[2]
    mel_bins = params[3]
    sample_rate = 8000

    wav_file = tf.strings.split(wav_path, os.path.sep)[-1]
    file_specs = tf.strings.split(wav_file, ".")[0]
    digit = tf.strings.to_number(tf.strings.split(file_specs, "_")[0], out_type = tf.int32)
    wavfile = tf.io.read_file(wav_path)
    sample, _ = tf.audio.decode_wav(wavfile)
    sample = tf.squeeze(sample, axis=-1)
    fixed_size = tf.constant([sample_len])
    sample_shape = tf.shape(sample)
    def pad_func():
        pad_size = fixed_size - sample_shape
        padding = tf.concat([tf.zeros_like(sample_shape), pad_size], axis=0)
        padding = tf.reshape(padding,(-1,2))
        return tf.pad(sample, padding)
    def slice_func():
        return tf.slice(sample, tf.constant([0]), fixed_size)
    
    sample = tf.cond(sample_shape > fixed_size, slice_func, pad_func)

    spectrogram = tf.signal.stft(sample, frame_length = fft_len, frame_step= step)
    spectrogram = tf.abs(spectrogram)

    num_spectrogram_bins = fft_len // 2 + 1  # spectrogram.shape[-1]
    lower_edge_hertz, upper_edge_hertz = 40.0, sample_rate / 2
    linear_to_mel_weight_matrix = tf.signal.linear_to_mel_weight_matrix(
      mel_bins, num_spectrogram_bins, sample_rate, lower_edge_hertz,
      upper_edge_hertz)
    mel_spectrograms = tf.tensordot(spectrogram, linear_to_mel_weight_matrix, 1)
    mel_spectrograms.set_shape(spectrogram.shape[:-1].concatenate(linear_to_mel_weight_matrix.shape[-1:]))

    # Compute a stabilized log to get log-magnitude mel-scale spectrograms.
    log_mel_spectrograms = tf.math.log(mel_spectrograms + 1e-6)
    avg = tf.math.reduce_mean(log_mel_spectrograms)
    std = tf.math.reduce_std(log_mel_spectrograms)
    normalized_mel = (log_mel_spectrograms - avg) / std
    normalized_mel = normalized_mel[..., tf.newaxis]

    return normalized_mel, digit

def create_datasets(sample_length, fft_size, step_size, batch_size, mel_bins):
    recordings_path = os.path.join(FSDD_PATH, "*.wav")
    ds = tf.data.Dataset.list_files(recordings_path)
    ds_size = tf.data.experimental.cardinality(ds).numpy()
    ds = ds.map(lambda x: mel_spectrogram(x, (sample_length, fft_size, step_size, mel_bins))).shuffle(ds_size)
    train_ds = ds.take(int(0.8 * ds_size))
    val_ds = ds.skip(int(0.8 * ds_size))
    test_ds = val_ds.shard(num_shards=2, index=0)
    val_ds = val_ds.shard(num_shards=2, index=1)

    train_ds = train_ds.batch(batch_size).cache().prefetch(tf.data.AUTOTUNE)
    val_ds = val_ds.batch(batch_size).cache().prefetch(tf.data.AUTOTUNE)
    test_ds = test_ds.batch(batch_size).cache().prefetch(tf.data.AUTOTUNE)
    spec_shape = (sample_length // step_size -1, mel_bins, 1)
    return train_ds, val_ds, test_ds, spec_shape