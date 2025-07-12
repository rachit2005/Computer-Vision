import cv2
import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Pencil Sketch Converter", layout="centered")
st.title("🖼️ Pencil Sketch Converter")

def convert_to_sketch(image: np.ndarray):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    return sketch

def image_to_bytes(pil_img: Image.Image):
    buf = BytesIO()
    pil_img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file:
    # Read file into OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Display original image
    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB")

    # Convert to sketch
    sketch_img = convert_to_sketch(img)
    sketch_pil = Image.fromarray(sketch_img)

    # Display sketch
    st.subheader("Sketch Image")
    st.image(sketch_pil, caption="Pencil Sketch", use_column_width=True)

    # Save/download button
    img_bytes = image_to_bytes(sketch_pil)

    filename = st.text_input("FileName", "", 30).strip()
    if not filename:
        filename="sketch"

    st.download_button(
        label="💾 Download Sketch as PNG",
        data=img_bytes,
        file_name=f"{filename}.png",
        mime="image/png",
    )
