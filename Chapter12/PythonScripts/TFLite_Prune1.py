import os.path as osp
import numpy as np
import tensorflow as tf
import tensorflow_model_optimization as tfmot
import tempfile

DATA_DIR = "classification_data"
MODEL_DIR = "models"

train_samples = np.load(osp.join(DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(osp.join(DATA_DIR, "cls_train_labels.npy"))
test_samples = np.load(osp.join(DATA_DIR, "cls_test_samples.npy"))
test_labels = np.load(osp.join(DATA_DIR, "cls_test_labels.npy"))

saved_model_dir='models/nn_classification_model_tf'

model = tf.keras.models.load_model(saved_model_dir)
model.summary()

baseline_model_accuracy = model.evaluate(test_samples, test_labels, verbose=0)
prune_low_magnitude = tfmot.sparsity.keras.prune_low_magnitude

# Compute end step to finish pruning after 2 epochs.
batch_size = 128
epochs = 2
validation_split = 0.1 # 10% of training set will be used for validation set.

num_samples = train_samples.shape[0] * (1 - validation_split)
end_step = np.ceil(num_samples/batch_size).astype(np.int32) * epochs

pruning_params = {
'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(
initial_sparsity=0.50,
final_sparsity=0.80,
begin_step=0,
end_step=end_step)
}

model_for_pruning = prune_low_magnitude(model, **pruning_params)
model_for_pruning.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(),
                       tf.keras.metrics.FalseNegatives()])
model_for_pruning.summary()

logdir = tempfile.mkdtemp()

callbacks = [
tfmot.sparsity.keras.UpdatePruningStep(),
tfmot.sparsity.keras.PruningSummaries(log_dir=logdir),
]

model_for_pruning.fit(train_samples,train_labels,epochs=2,validation_split=0.1, callbacks=callbacks)
model_for_pruning_accuracy = model_for_pruning.evaluate(test_samples, test_labels, verbose=0)

print('Baseline test accuracy:', baseline_model_accuracy)
print('Pruned test accuracy:', model_for_pruning_accuracy)

model_for_export = tfmot.sparsity.keras.strip_pruning(model_for_pruning)
pruned_keras_file = 'models/pruned_model.h5'
tf.keras.models.save_model(model_for_export, pruned_keras_file, include_optimizer=False)