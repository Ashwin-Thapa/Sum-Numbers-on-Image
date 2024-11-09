import easyocr
from PIL import Image
import numpy as np
import re
import streamlit as st

def extract_text_with_easyocr(image):
    reader = easyocr.Reader(['en'])
    
    # Convert the image file to an OpenCV-compatible format
    image = Image.open(image)  # Open the image with PIL
    image = np.array(image)    # Convert the PIL image to a NumPy array
    
    # Read text using EasyOCR
    results = reader.readtext(image)
    extracted_text = " ".join([text for _, text, _ in results])
    st.write("Extracted Text with EasyOCR:", extracted_text)
    return extracted_text

def extract_numbers_and_calculate_sum(text):
    numbers = re.findall(r'\d+', text)
    numbers = list(map(int, numbers))
    total_sum = sum(numbers)
    st.write("Extracted numbers:", numbers)
    st.write("Sum of numbers:", total_sum)
    return total_sum

def main():
    st.title("Image Text Extraction and Number Summation")
    
    # Allow user to upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract text and calculate sum if EasyOCR is enabled
        text = extract_text_with_easyocr(uploaded_file)
        total_sum = extract_numbers_and_calculate_sum(text)
        st.write("Total sum of numbers in the image:", total_sum)

if __name__ == "__main__":
    main()
