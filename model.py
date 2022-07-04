import streamlit as st
import torch
#from torchvision import transforms
from PIL import Image
import os
import shutil
import glob
from realesrgan import RealESRGAN
import numpy as np
#print(torch.cuda.is_available())


def run_model(image):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('device:', device)
    model = RealESRGAN(device, scale=2)
    model.load_weights('weights/RealESRGAN_x2.pth')
    # enhance image
    image_array = Image.open(image).convert('RGB')
    sr_image = model.predict(np.array(image_array))
    return sr_image

st.write(
    """
# The picture enhancer
Upload your pics
"""
)

uploaded_file = st.file_uploader("Upload your image")

if uploaded_file:
    st.write("Original image")
    st.image(uploaded_file)
    st.write("Enhancing the image")
    result = run_model(uploaded_file)
    st.image(result)
    st.download_button('Download file', result)