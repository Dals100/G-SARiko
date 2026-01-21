import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="G-SARiko", layout="wide")

st.title("🎨 G-SARiko - Image Enhancement")
st.write("Améliquez vos photos comme Google Pixel !")

# Sidebar pour les options
st.sidebar.header("⚙️ Options")

# Upload d'image
uploaded_file = st.file_uploader("Téléchargez votre image", type=["jpg", "jpeg", "png"]) 

if uploaded_file is not None:
    # Lire l'image
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    # Afficher l'image originale
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Image Originale")
        st.image(image, use_column_width=True)
    
    # Options d'amélioration
    st.sidebar.subheader("Améliorations disponibles")
    
    enhance_brightness = st.sidebar.slider("Luminosité", 0.5, 2.0, 1.0)
    enhance_contrast = st.sidebar.slider("Contraste", 0.5, 2.0, 1.0)
    enhance_sharpness = st.sidebar.slider("Netteté", 0.0, 2.0, 1.0)
    
    # Appliquer les améliorations
    enhanced_img = cv2.convertScaleAbs(img_array, alpha=enhance_contrast, beta=0)
    enhanced_img = cv2.convertScaleAbs(enhanced_img, alpha=enhance_brightness, beta=0)
    
    if enhance_sharpness > 0:
        kernel = np.array([[-1, -1, -1],
                          [-1,  9 + enhance_sharpness, -1],
                          [-1, -1, -1]]) / (1 + enhance_sharpness)
        enhanced_img = cv2.filter2D(enhanced_img, -1, kernel)
    
    enhanced_img = cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2RGB)
    enhanced_img_pil = Image.fromarray(enhanced_img.astype('uint8'))
    
    # Afficher l'image améliorée
    with col2:
        st.subheader("Image Améliorée")
        st.image(enhanced_img_pil, use_column_width=True)
    
    # Bouton de téléchargement
    st.subheader("📥 Télécharger l'image")
    buf = io.BytesIO()
    enhanced_img_pil.save(buf, format="PNG")
    buf.seek(0)
    
    st.download_button(
        label="Télécharger l'image améliorée",
        data=buf.getvalue(),
        file_name="image_amelioree.png",
        mime="image/png"
    )
else:
    st.info("👆 Téléchargez une image pour commencer !")