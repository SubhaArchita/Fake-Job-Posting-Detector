# Fake Job Posting Detector

Overview:
  The Fake Job Posting Detector is a machine learning-powered web app that helps users detect potentially fake job postings based on the description text. It uses Natural Language Processing (NLP) and a logistic      regression model trained on real world job data.
<br>
Features:
<br>
  - Paste any job description and detect if it’s fake
  -  See a confidence score (% chance it's fake or real)
  -  Clean, interactive UI powered by Streamlit
  -  Trained model using TF-IDF + Logistic Regression
  -  Works entirely offline after setup
  -  Simple codebase for learning NLP, ML, and deployment
<br>
Tech Stack:
<br>
 -  Python
 -  Streamlit – for web interface
 -  Scikit-learn – model training + prediction
 -  Joblib – model persistence
 -  Pandas – data handling
<br>
Model Info:
<br>
  - Model: Logistic Regression
  - Text Preprocessing: TF-IDF Vectorization
  - Training Data: Based on the [Fake Job Postings Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)
  - Accuracy: ~92% on test set
<br>
Author:
<br>
  N. Subha Archita
<br>
  [GitHub](https://github.com/SubhaArchita) | [LinkedIn](https://www.linkedin.com/in/nsubhaarchita/)
