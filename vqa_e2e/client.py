import streamlit as st
import requests
from PIL import Image
import io
import json
import base64

# URL = 'http://127.0.0.1:8000/predict'
URL = 'http://localhost:8000/predict'

def main():
    st.title("Image Upload and Processing")

    # uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    question = st.text_input('Query', 'What is this?')
        
    if st.button('Submit'):
        response = requests.post(URL, data = json.dumps({"input_question" : question}))
        if response.status_code == 200:
            result = response.json()
        else:
            result = response.text
            
        st.write(f"Answer: {result}")

if __name__ == "__main__":
    main()
