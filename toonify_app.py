#!/usr/bin/env python3
#import cv2 as cv
import streamlit as st
import requests
import json
from PIL import Image
import requests
from io import BytesIO

# ***********************************
# MAIN
# ***********************************
st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Caricaturizador")
st.header("Hola! soy el dibujante de createch y haré una caricatura de tu foto :smile:")
#st.markdown("Hola! soy **creaRec**, el primer reconocedor de createch :smile:")

st.subheader("Sube una imagen tipo selfie")

uploaded_file = st.file_uploader("", type="jpg")
if uploaded_file is not None:

    r = requests.post(
        "https://api.deepai.org/api/toonify",
        files={
            'image': open(uploaded_file, 'rb'),
        },
        headers={'api-key': 'ed22d0b2-4cc5-4223-9e48-302f8a86c7c5'}
    )
    #print(r.json())
    imgURL = r['output_url']
    response = requests.get(imgURL)
    img = Image.open(BytesIO(response.content))

    #caraTest_cv=cv.cvtColor(caraTest,cv.COLOR_BGR2RGB)
    st.subheader("Este es el resultado:")
    st.image(img, caption='', use_column_width=True)
    st.subheader("Hasta luego!")
        
