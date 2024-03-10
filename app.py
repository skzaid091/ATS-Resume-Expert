from dotenv import load_dotenv

load_dotenv()

import os
import base64
import streamlit as st
from PIL import Image
import pdf2image
import google.generativeai as genai
import io

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_genimi_response(input, pdf_content, prompt):

    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text


def input_pdf_setup(uploaded_file):

    if uploaded_file is not None:

        ## Convert the PDf to Image
        ## images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path='C:/Program Files/poppler-24.02.0/Library/bin')
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        ## Convert to Bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type" : "image/jpeg",
                "data" : base64.b64encode(img_byte_arr).decode() # encode to base64
            }
        ]

        return pdf_parts

    else :
        raise FileNotFoundError("No File Uploaded")
    

# STREAMLIT APP
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description : ", key="input")

uploaded_file = st.file_uploader("Upload your Resume(PDF).... ", type=["pdf"])

if uploaded_file is not None:

    st.write("File Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")

submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scale the resume against the provided job description. Give me the percentage of 
match if the resume matches the job description. First the output should come as percentage as "Match Percentsge : " in the First Line then a blank line and 
then keywords which are missing in the resume as "Missing Keywords : " in a well structured format with numbering or commas and then again a blank line and lastnner with a deep understanding a final thought about the
resume that is it capable of being selected for the job description and suggestions that can be done to increase the match percentage for the
job description as "Final Thoughts : ".
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_genimi_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("Please upload the Resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_genimi_response(input_prompt3, pdf_content, input_text)
        st.write("                                                          ")
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("Please upload the Resume")
