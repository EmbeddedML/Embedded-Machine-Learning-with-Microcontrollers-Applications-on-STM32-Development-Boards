import os.path as osp
import numpy as np
import tensorflow as tf
import tensorflow_model_optimization as tfmot

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

clustering_params = {
  'number_of_clusters': 16,
  'cluster_centroids_init': tfmot.clustering.keras.CentroidInitialization.LINEAR
}

# Cluster a whole model
clustered_model = tfmot.clustering.keras.cluster_weights(model, **clustering_params)

# Use smaller learning rate for fine-tuning clustered model
clustered_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(),
                       tf.keras.metrics.FalseNegatives()])

clustered_model.summary()

clustered_model.fit(train_samples, train_labels, batch_size=500, epochs=1, validation_split=0.1)
clustered_model_accuracy = clustered_model.evaluate(test_samples, test_labels, verbose=0)

print('Baseline test accuracy:', baseline_model_accuracy)
print('Clustered test accuracy:', clustered_model_accuracy)

# Create 6x smaller models from clustering
model_for_export = tfmot.clustering.keras.strip_clustering(clustered_model)
clustered_keras_file = 'models/clustered_model.h5'
tf.keras.models.save_model(model_for_export, clustered_keras_file, include_optimizer=False)