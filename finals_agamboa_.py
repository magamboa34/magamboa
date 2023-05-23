# -*- coding: utf-8 -*-
"""Finals_AGamboa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19mr-CJmUL9BhZO99THNI1SufzMAhUSdX
"""

import streamlit as st
import tensorflow as tf


@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('malaria_detector.h5')
  return model
model=load_model()
st.write("""
# Malaria Detector"""
)
file=st.file_uploader("Choose A Laboratory Sample",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(130,130)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['PARASITIZED','UNINFECTED']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)
