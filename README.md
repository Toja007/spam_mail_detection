#                                                                                Spam Mail Detection Model
![images](https://github.com/Toja007/spam_mail_detection/assets/131866743/95bc50de-efc7-467b-b457-ab0518fbc6fc)


# Overview
This repository contains a spam mail detection model developed using machine learning techniques. The model is designed to classify emails as either "spam" or "ham" (non-spam), providing a useful tool for email filtering and spam detection.

# Model Behavior
The spam mail detection model behaves as follows:

If an email is classified as spam, the model returns "spam."
If an email is classified as non-spam, the model returns "ham."
# Dataset
The spam mail detection model was trained and tested using a labeled dataset consisting of email samples categorized into spam and non-spam categories. The dataset was preprocessed to handle text normalization, tokenization, and feature extraction before training the classification model.

# Model Architecture
The spam mail detection model is based on a logistic regression, and random forest classifier. The model utilizes techniques like TF-IDF (Term Frequency-Inverse Document Frequency), feature engineering, and hyperparameter tuning to achieve accurate classification of spam and non-spam emails.

# Performance Evaluation
The model's performance is evaluated using classification accuracy. These metrics provide insights into the model's ability to correctly classify spam and non-spam emails.

# Usage
To use the spam mail detection model:

Clone this repository to your local machine.
Install the necessary dependencies, such as Python, scikit-learn, and Streamlit.
Download or prepare your own email data for spam detection.
Preprocess the email data, including text normalization, tokenization, and feature extraction.
Load the trained classification model or train a new model using the provided code or scripts.
Use the model to predict whether an email is spam ("spam") or non-spam ("ham").
Streamlit Application
A Streamlit application named "spam_mail_app.py" is included in this repository. You can run the Streamlit app locally to interactively test the spam mail detection model and input your own email samples to see the model's predictions.

<img width="808" alt="spm" src="https://github.com/Toja007/spam_mail_detection/assets/131866743/8bd48e58-00a7-42f6-8957-ebdb04d4dac3">


# To run the Streamlit app:

Install Streamlit by running pip install streamlit.
Navigate to the directory containing "spam_mail_app.py" in your terminal.
Run the command streamlit run app_spam.py.
Access the Streamlit app in your web browser to use the spam mail detection model.
