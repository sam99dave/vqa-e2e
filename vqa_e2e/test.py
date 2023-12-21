import streamlit as st
from PIL import Image
import io


def process_image(uploaded_image):
    print(type(uploaded_image))
    img = Image.open(uploaded_image)
    # Perform image processing operations here if needed
    return img


def main():
    st.title("Image Upload and Processing")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image_bytes = uploaded_file.read()
        print(type(image_bytes))
        image = process_image(io.BytesIO(image_bytes))
        st.image(image, caption="Uploaded Image", use_column_width=True)


if __name__ == "__main__":
    main()
