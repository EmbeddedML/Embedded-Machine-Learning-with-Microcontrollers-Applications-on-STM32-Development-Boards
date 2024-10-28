import os
from keras import optimizers
from keras import losses
from keras.callbacks import ModelCheckpoint, EarlyStopping
from Models.paths import KERAS_MODEL_DIR
from .data_loader import create_datasets
from ..PythonScripts.resnet import ResNet

train_ds, val_ds, test_ds, input_shape = create_datasets(8000, 512, 256, 32)
kws_cnn_model = ResNet(10, input_shape, 2)
kws_cnn_model.compile(
    optimizer=optimizers.Adam(0.0005, weight_decay=1e-6),
    loss=losses.SparseCategoricalCrossentropy(),
    metrics="accuracy",
)
model_cp_callback = ModelCheckpoint(
    os.path.join(KERAS_MODEL_DIR, "kws_cnn.h5"), save_best_only=True
)
es_callback = EarlyStopping(verbose=1, patience=5)
kws_cnn_model.fit(
    train_ds,
    epochs=50,
    validation_data=val_ds,
    verbose=1,
    callbacks=[model_cp_callback, es_callback],
)
