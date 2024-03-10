# 🚀 ATS Resume Expert

Welcome to ATS Resume Expert, an Applicant Tracking System (ATS) powered by Google's Generative AI. This Streamlit application helps you analyze resumes against job descriptions with ease.

## Features

- **PDF to Image Conversion:** Converts uploaded PDF resumes into images for analysis.
- **AI-Powered Evaluation:** Utilizes Google's Generative AI to provide professional evaluations of resumes based on job descriptions.
- **Percentage Match Calculation:** Calculates the percentage match between resumes and job descriptions, along with detailed insights.

## Getting Started

### Prerequisites

1. Ensure you have Python installed on your machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Get your Google API key and set it in the `.env` file.
   (https://aistudio.google.com/app/apikey) go to this link and login if required and hit the Button "Create API Key" and copy that API Key and paste it in .env file.
4. You need to install "poppler" but don't worry I've attached a directly downloaded folder as a zip with this repo named as "poppler-24.02.0" just unzip it and move the folder the to following path "C:\Program Files".
5. If the poppler's folder location is different than the above then update this line in the code as "poppler_path='Location to the Folder".


### SCREENSHOTS
![App Screenshot 2](/screenshots/Picture1.jpg)
![App Screenshot 2](/screenshots/Picture2.jpg)
![App Screenshot 2](/screenshots/Picture3.jpg)


### Running the Application

```bash
streamlit run app.py
'''
