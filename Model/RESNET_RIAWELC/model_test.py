import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

#Testa o modelo sem a divisão por pacotes

model_path = 'best_model.keras'

model = load_model(model_path)

img_path = 'img_path'
img = tf.keras.utils.load_img(img_path, target_size=(256, 256))

img_array = tf.keras.utils.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

img_array = img_array / 255.0

prediction = model.predict(img_array)

if prediction[0] > 0.5:
    print("Sem defeito")
else:
    print("Com defeito")

classe_predita = np.argmax(prediction)
print(f"Classe Predita: {classe_predita}")
