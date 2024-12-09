import cv2
import numpy as np
import streamlit as st
from PIL import Image

def enhance_image(image):
    # Convert the image to a NumPy array
    img = np.array(image)
    
    # Convert the image to YUV color space
    yuv_img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    
    # Equalize the histogram of the Y channel (luminance)
    yuv_img[:, :, 0] = cv2.equalizeHist(yuv_img[:, :, 0])
    
    # Convert the YUV image back to RGB format
    enhanced_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2RGB)
    return enhanced_img

st.title("Low-Light Image Enhancement")

# Upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    input_image = Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(input_image, caption="Uploaded Image", use_column_width=True)
    
    # Enhance the image
    enhanced_image = enhance_image(input_image)
    
    # Display the enhanced image
    st.subheader("Enhanced Image")
    st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)
    
    # Option to download the enhanced image
    st.subheader("Download Enhanced Image")
    enhanced_image_pil = Image.fromarray(enhanced_image)
    st.download_button(
        label="Download Image",
        data=enhanced_image_pil.tobytes(),
        file_name="enhanced_image.jpg",
        mime="image/jpeg"
    )
