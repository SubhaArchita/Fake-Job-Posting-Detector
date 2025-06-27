import joblib
import streamlit as st

model = joblib.load('jobs.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("Fake Job Posting Detector")
st.markdown("Paste your job posting here")

text_inp = st.text_area("Job Description", height=300)

if st.button("Check"):
    try:
        vector = vectorizer.transform([text_inp])
        predict = model.predict(vector)[0]
        probability = model.predict_proba(vector)

        fake_p = round(probability[0][1] * 100, 2)
        real_p = round(probability[0][0] * 100, 2)

        if predict == 1:
            st.error(f"This might be {fake_p}% Fake and {real_p}% Real")
        else:
            st.success(f"This might be {real_p}% Real and {fake_p}% Fake")
    
    except Exception as e:
        st.exception(f"Prediction Failed: {e}")