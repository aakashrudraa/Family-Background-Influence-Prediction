# 🏡 Family Background Influence Prediction

An end-to-end Machine Learning web application that predicts an individual's:

- 🎯 Self-Efficacy Score
- 💼 Career Success Expectation Score
- 🌟 Life Success Expectation Score

based on family background information using Gradient Boosting Regression models.

---

## 🚀 Live Demo

🔗 https://your-streamlit-app-url.streamlit.app

---

## 📌 Features

- Predicts three psychological scores simultaneously.
- Interactive Streamlit web interface.
- User-friendly questionnaire.
- Compares predicted scores with actual questionnaire scores.
- Trained using Machine Learning with hyperparameter tuning.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas
- Joblib

---

## 📂 Project Structure

```
Family-Background-Influence-Prediction/
│
├── prediction.py
├── Family_trained_model.pkl
├── requirements.txt
├── README.md
└── pages/
    └── Questionnaire.py
```

---

## 📊 Machine Learning Pipeline

1. Data Cleaning
2. Feature Encoding
3. Train-Test Split
4. Hyperparameter Tuning (RandomizedSearchCV)
5. Gradient Boosting Regression
6. Model Evaluation
7. Model Serialization using Joblib
8. Streamlit Deployment

---

## 📈 Input Features

- Gender
- Age
- City Type
- Father's Occupation
- Mother's Occupation
- Father's Qualification
- Mother's Qualification
- Father's Annual Income
- Mother's Annual Income
- Other Family Income

---

## 🎯 Predicted Outputs

- Self-Efficacy Score
- Career Success Expectation Score
- Life Success Expectation Score

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/aakashrudraa/Family-Background-Influence-Prediction.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run prediction.py
```

---

## 📸 Screenshots

(Add screenshots of your web application here.)

---

## 👨‍💻 Author

**Aakash Rudra**

Mechanical Engineering Undergraduate  
Indian Institute of Technology Madras

GitHub: https://github.com/aakashrudraa

---

## ⭐ Future Improvements

- More advanced ML models
- Explainable AI (SHAP)
- Better UI/UX
- User authentication
- Cloud database integration

---

## 📜 License

This project is licensed under the MIT License.
