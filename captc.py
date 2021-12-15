from tensorflow import keras
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16,preprocess_input,decode_predictions
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

#model = VGG16(weights='imagenet')
model = keras.models.load_model('mnist_model.h5')
k = ["metal","glass"]
#model = VGG16()
#print(model.summary())
load_model
image = load_img("images/1.png",target_size=(28,28))
image = img_to_array(image)
image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
image = preprocess_input(image)
y_pred = model.predict(image)
print(int(y_pred[0][0]))
