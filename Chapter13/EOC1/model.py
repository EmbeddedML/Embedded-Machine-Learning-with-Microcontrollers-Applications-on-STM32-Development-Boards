from keras import layers, models, losses,optimizers

def normalize_input(input_ds):
    norm_layer = layers.Normalization()
    norm_layer.adapt(input_ds.map(map_func=lambda spec, label: spec))
    return norm_layer

def create_model(input_shape, num_labels, norm_layer):
    cnn_model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.Resizing(32,32),
        norm_layer,
        layers.Conv2D(32, 3, activation='relu'),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.25),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_labels),
    ])

    cnn_model.compile(optimizer = optimizers.Adam(0.0005, weight_decay = 1e-6),
                      loss = losses.SparseCategoricalCrossentropy(from_logits=True),
                       metrics="accuracy")

    return cnn_model
