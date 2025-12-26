import streamlit as st
import pickle

# Load saved model and vectorizer
model = pickle.load(open("final_fake_job_svm_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# App title
st.title("Fake Job Posting Detection")

st.write("Paste a job description below to check if it is REAL or FAKE.")

# Text input from user
job_text = st.text_area("Job Description")

# Button
if st.button("Check Job"):
    if job_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        job_vec = tfidf.transform([job_text])
        prediction = model.predict(job_vec)

        if prediction[0] == 1:
            st.error("This looks like a FAKE job posting")
        else:
            st.success("This looks like a REAL job posting")
