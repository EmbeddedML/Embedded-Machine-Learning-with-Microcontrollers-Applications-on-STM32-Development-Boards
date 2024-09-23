import os
import tensorflow as tf
from Data.paths import FSDD_PATH
    
def split_fn(wav_path, train):
    file_specs = tf.strings.split(wav_path, ".")[0]
    file_specs = tf.strings.split(file_specs, os.path.sep)[1]
    person = tf.strings.split(file_specs, "_")[1]
    if train:
        return person != b"yweweler"
    else:
        return person == b"yweweler"

def get_spectrogram(wav_path, audio_params):
    wav_file = tf.strings.split(wav_path, os.path.sep)[-1]
    file_specs = tf.strings.split(wav_file, ".")[0]
    digit = tf.strings.to_number(tf.strings.split(file_specs, "_")[0], out_type = tf.int32)
    wavfile = tf.io.read_file(wav_path)
    sample, _ = tf.audio.decode_wav(wavfile)
    sample = tf.squeeze(sample, axis=-1)
    fixed_size = tf.constant([audio_params[0]])
    sample_shape = tf.shape(sample)
    def pad_func():
        pad_size = fixed_size - sample_shape
        padding = tf.concat([tf.zeros_like(sample_shape), pad_size], axis=0)
        padding = tf.reshape(padding,(-1,2))
        return tf.pad(sample, padding)
    def slice_func():
        return tf.slice(sample, tf.constant([0]), fixed_size)
    
    sample = tf.cond(sample_shape > fixed_size, slice_func, pad_func)

    spectrogram = tf.signal.stft(sample, frame_length=audio_params[1], frame_step=audio_params[2])
    spectrogram = tf.abs(spectrogram)
    spectrogram = spectrogram[..., tf.newaxis]
    return spectrogram, digit

def create_datasets(sample_length, fft_size, step_size, batch_size):
    recordings_path = os.path.join(FSDD_PATH, "*.wav")
    ds = tf.data.Dataset.list_files(recordings_path)
    ds_size = tf.data.experimental.cardinality(ds).numpy()
    ds = ds.map(lambda x: get_spectrogram(x, (sample_length, fft_size, step_size))).shuffle(ds_size)
    train_ds = ds.take(int(0.8 * ds_size))
    val_ds = ds.skip(int(0.8 * ds_size))
    test_ds = val_ds.shard(num_shards=2, index=0)
    val_ds = val_ds.shard(num_shards=2, index=1)

    train_ds = train_ds.batch(batch_size).cache().prefetch(tf.data.AUTOTUNE)
    val_ds = val_ds.batch(batch_size).cache().prefetch(tf.data.AUTOTUNE)
    test_ds = test_ds.batch(batch_size).cache().prefetch(tf.data.AUTOTUNE)
    spec_shape = (sample_length // step_size -1, step_size + 1, 1)
    return train_ds, val_ds, test_ds, spec_shape