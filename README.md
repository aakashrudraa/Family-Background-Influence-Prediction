# Family-Background-Influence-Prediction


## Overview

This project explores how different aspects of a student's family background may relate to their psychological outlook. Using machine learning, the application predicts three important indicators:

- Self-Efficacy
- Career Success Expectation
- Life Success Expectation

The user enters information about their family background, such as parents' education, occupation, income, city type, and other demographic details. The trained model then predicts scores for these three indicators and provides an interpretation of the results.

**Note:** The predictions are based on patterns learned from the training dataset. They are intended for educational and research purposes and should not be considered psychological or clinical assessments.

---

## Motivation

Family environment plays an important role in shaping a person's confidence, career aspirations, and expectations about the future. This project was built to understand these relationships using data-driven methods.

The objective is not to judge an individual but to demonstrate how machine learning can be applied to social science and educational datasets to discover meaningful patterns.

---

## Features

- Predicts three psychological indicators from family background information.
- Clean and interactive Streamlit interface.
- Questionnaire to compare predicted scores with actual self-reported scores.
- Easy-to-understand interpretation of prediction results.
- End-to-end machine learning pipeline from training to deployment.

---

## Machine Learning Workflow

1. Data preprocessing
2. Feature encoding
3. Model training
4. Hyperparameter tuning using RandomizedSearchCV
5. Model evaluation
6. Model serialization using Joblib
7. Streamlit web application deployment

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## Input Features

The model uses the following information:

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

## Model Output

The application predicts:

- Self-Efficacy Score
- Career Success Expectation Score
- Life Success Expectation Score

Each prediction is accompanied by a qualitative interpretation to help users understand the result.

---

## Project Structure

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

## Running the Project

Clone the repository

```bash
git clone https://github.com/aakashrudraa/Family-Background-Influence-Prediction.git
```

Move into the project directory

```bash
cd Family-Background-Influence-Prediction
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run prediction.py
```

---

## Future Improvements

- Improve model accuracy with more diverse datasets.
- Add explainable AI techniques such as SHAP values.
- Generate downloadable personalized reports.
- Improve UI/UX.
- Support multiple languages.

---

## Acknowledgements

This project was developed as part of my machine learning learning journey to gain practical experience in data preprocessing, model building, hyperparameter tuning, deployment, and building interactive ML applications.

---

## Author

**Aakash Rudra**

B.Tech Mechanical Engineering  
Indian Institute of Technology Madras

GitHub: https://github.com/aakashrudraa