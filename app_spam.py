import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import re

# Load the trained model
model = pickle.load(open("spam_model.pkl", 'rb'))

# Load the CountVectorizer
vectorizer = pickle.load(open("vectorizer_spam.pkl", 'rb'))

# Function to preprocess text
def preprocess_text(text):
    pattern = r'[^a-zA-Z0-9\s]'
    # Use re.sub to replace the matched pattern with an empty string
    text = re.sub(pattern, '', text)
    text = str.lower(text)
    return text

# Function to predict spam
def predict_spam(text):
    text = preprocess_text(text)
    text = vectorizer.transform([text])
    pred = model.predict(text)
    return pred[0]

# Streamlit app
def main():
    # Custom CSS for font styling
    st.markdown(
        """
        <style>
            .title {
                font-family: 'Verdana', sans-serif;
                font-size: 36px;
                color: #FFFFFF;
                text-align: center;
                padding-top: 30px;
            }
            .text-area {
                font-family: 'Arial', sans-serif;
                font-size: 16px;
                color: #000000;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #CCCCCC;
            }
            .button {
                font-family: 'Arial', sans-serif;
                font-size: 18px;
                color: #FFFFFF;
                background-color: #008080;
                border-radius: 5px;
                padding: 10px 20px;
                margin-top: 20px;
            }
            .footer {
                font-family: 'Arial', sans-serif;
                font-size: 14px;
                color: #FFFFFF;
                text-align: center;
                padding-top: 30px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title with stylish font
    st.markdown("<h1 class='title'>Spam Email Classifier</h1>", unsafe_allow_html=True)

    # Background image
    st.markdown(
        """
        <style>
            body {
                background-image: url("caution.jpg");
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.write('Enter an email to classify it as spam or ham.')

    # Text input for user to enter email with custom styling
    email_text = st.text_area('Enter email text', '', height=150, key='email_text', placeholder='Type your email here...')

    # Button to predict with animation
    if st.button('Predict'):
        if email_text:
            with st.spinner('Classifying...'):
                prediction = predict_spam(email_text)
                if prediction == 'spam':
                    st.error('Spam Email')
                else:
                    st.success('Ham Email')
        else:
            st.warning('Please enter some text.')

    # Add footer
    st.markdown("<p class='footer'>Made with ❤️ by T-spice</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
