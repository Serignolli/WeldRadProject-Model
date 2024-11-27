from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from resnet_model import create_resnet_model
import matplotlib.pyplot as plt

#Treinamento do modelo

input_shape = (256, 256, 3)
batch_size = 32
epochs = 20
learning_rate = 0.0001
data_path = 'path'

datagen = ImageDataGenerator(validation_split=0.2, rescale=1./255)

train_data = datagen.flow_from_0directory(
    data_path,
    target_size=(256, 256),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

validation_data = datagen.flow_from_directory(
    data_path,
    target_size=(256, 256),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

model = create_resnet_model(input_shape)

model.compile(optimizer=Adam(learning_rate=learning_rate),
              loss='binary_crossentropy',
              metrics=['accuracy'])

callbacks = [
    ModelCheckpoint('best_model.keras', monitor='val_loss', save_best_only=True, verbose=1),
    EarlyStopping(monitor='val_loss', patience=5, verbose=1, restore_best_weights=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, verbose=1, min_lr=1e-6)
]

history = model.fit(
    train_data,
    validation_data=validation_data,
    epochs=epochs,
    callbacks=callbacks
)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()

model.save('resnet_rialwelc_model.keras')