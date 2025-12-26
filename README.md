# Fake-Job-Posting-Detection
An NLP-based machine learning system to detect fake job postings

# Fake Job Posting Detection using Machine Learning

## 📌 Overview
This project aims to detect fraudulent job postings using Machine Learning
and Natural Language Processing (NLP) techniques. The system classifies job
descriptions as **Real** or **Fake** based on textual content.

---

## 🎯 Problem Statement
Online job portals are increasingly exploited by scammers. This project
automatically identifies fake job advertisements to protect job seekers.

---

## 🧠 Approach
- Data preprocessing and cleaning
- Text feature extraction using TF-IDF
- Training multiple classification models
- Model comparison using F1-score
- Selection of best-performing model (Linear SVM)
- Deployment using Streamlit

---

## 📊 Dataset
- Source: Public Kaggle Fake Job Postings Dataset
- Records: ~18,000
- Target variable:
  - `0` → Real Job
  - `1` → Fake Job

---

## 🤖 Models Used
- Logistic Regression
- Naive Bayes
- Linear Support Vector Machine (SVM)

Linear SVM was selected based on the best F1-score
and lower false-negative rate.

---

## 📈 Evaluation
- Precision
- Recall
- F1-score
- Confusion Matrix
- Model comparison bar charts

---

## 🚀 Deployment
The final model was deployed using **Streamlit**.
Users can input job descriptions and get real-time predictions.

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF (NLP)
- Matplotlib, Seaborn
- Streamlit
