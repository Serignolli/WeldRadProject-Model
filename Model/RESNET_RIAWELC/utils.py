import tensorflow as tf
import os

#Pré-processamento das imagens
def load_and_preprocess_data(dataset_path, image_size, batch_size):

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        os.path.join(dataset_path, 'train'),
        image_size=image_size,
        batch_size=batch_size
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        os.path.join(dataset_path, 'val'),
        image_size=image_size,
        batch_size=batch_size
    )

    normalization_layer = tf.keras.layers.Rescaling(1. / 255)
    train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))

    return train_ds, val_ds
