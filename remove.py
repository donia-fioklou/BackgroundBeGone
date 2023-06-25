# un script python qui supprime l'arrière plan d'une image 
# et le stocke dans un le dossier "images" du projet

from io import BytesIO
from rembg import remove
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Remover de la mort", page_icon="🌈", layout="wide",)
st.write("# Supprimer l'arrière plan d'une image ")
st.write("## Upload une image et je te supprime l'arrière plan")
st.sidebar.write("## Uploader")

col1, col2 = st.columns(2)
# charger l'image

def convert_image(image):
    buffer=BytesIO()
    image.save(buffer, format="PNG")
    byte_image=buffer.getvalue()
    return byte_image

def fix_image(image):
    image=Image.open(image)
    col1.write("## Image originale")
    col1.image(image)
    fixed= remove(image)
    col2.write("## Image détourée")
    col2.image(fixed)
    col2.download_button("Télécharger l'image", convert_image(fixed), "imageDetoure.png", "midle")
    
    st.write("\n")
    st.sidebar.download_button("Télécharger l'image", convert_image(fixed), "imageDetoure.png", "")

image_upload=st.sidebar.file_uploader("choisissez une image", type=['jpg','png','jpeg'])

if image_upload is not None:
    fix_image(image_upload)
else:
    fix_image("./oiseaux.jpg") 
    


