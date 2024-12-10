import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
import tensorflow as tf
from tensorflow import keras
import os

st.markdown(f'''<div style = 'text-align:center; font-size:50px;'>SKIN CANCER CLASSIFICATION</div>
            ''', unsafe_allow_html=True)

def remove_all():
    test_path = 'G:\\Jupyter\\Deep_learning\\Projects\\Mini-Project-I(Skin Cancer Classification)\\tests'
    for i in os.listdir(test_path):
        path = os.path.join(test_path, i)
        os.remove(path)

def predict(image):
    models = 'G:\\Jupyter\\Deep_learning\\Projects\\Mini-Project-I(Skin Cancer Classification)\\models'
    model = keras.models.load_model(models + '\\Fruits360_EfficientNetB0.h5')
    image = cv2.imread(image)
    image = cv2.resize(image, (224,224))
    image = image * (1.0/255)
    image = np.expand_dims(image, axis=0)# 1,256,256,3
    preds = model.predict(image)
    # st.write(preds)
    classes = ['squamous cell carcinoma', 
               'pigmented benign keratosis', 
               'dermatofibroma', 'vascular lesion', 
               'actinic keratosis', 'seborrheic keratosis', 
               'melanoma', 'nevus', 'basal cell carcinoma']
    pred_class = classes[np.argmax(preds)]
    st.markdown(f'''<div style='font-size:25px; color:red;'>{pred_class}</div>''', unsafe_allow_html=True)
    
    
def get_image():

    st.markdown('''<h4 style = 'margin-top:2rem'>Choose an Image of Cancer</h4>''', 
                unsafe_allow_html=True)
    
    predict_image = st.file_uploader(label = ' ',type=['jpeg', 'jpg', 'png'])

    if predict_image is not None:
        st.image(predict_image, width=550, use_column_width=False, caption='')

        test_path = 'G:\\Jupyter\\Deep_learning\\Projects\\Mini-Project-I(Skin Cancer Classification)\\tests'
        save_path = test_path + '\\' + predict_image.name
    
        with open(save_path, 'wb') as file:
            file.write(predict_image.getbuffer())

        if st.button(label='Predict!'):
            predict(save_path)
        
get_image()

if(st.button("Clear Test Directory!")):
    remove_all()
