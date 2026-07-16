# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.


# import numpy as np
# import pickle 
# loaded_model=pickle.load(open("C:/Users/aakas/OneDrive/Desktop/Project/Project_1/Deploy/Family_trained_model.sav",'rb'))
# """
import numpy as np
import joblib
import streamlit as st

loaded_model = joblib.load("Family_trained_model.pkl")

def score_prediction(input_data):

    input_array = np.asarray(input_data).reshape(1,-1)

    prediction_se = loaded_model['model_se'].predict(input_array) #return array([some value])
    prediction_cse= loaded_model['model_cse'].predict(input_array)
    prediction_lse= loaded_model['model_lse'].predict(input_array)

    return prediction_se, prediction_cse, prediction_lse

    #if anything, i want to print on the basis of score

def main():

    
    # ---------------------- City ----------------------
    
    city_map = {
        "Village": 1,
        "Town": 2,
        "City": 3,
        "Metro": 4
    }
    
    # ---------------------- Qualification ----------------------
    
    qualification_map = {
        "No Formal": 0,
        "Primary": 1,
        "Middle": 2,
        "10th": 3,
        "12th": 4,
        "ITI": 5,
        "Diploma": 6,
        "Bachelor": 7,
        "Professional": 8,
        "Master": 9,
        "PhD": 10
    }
    
    # ---------------------- Occupation ----------------------
    
    occupation_map = {
        "Deceased": 0,
        "Unemployed": 1,
        "Labourer": 2,
        "Driver": 3,
        "Farmer": 3,
        "Shopkeeper": 4,
        "Homemaker": 5,
        "Corporate Employee": 6,
        "Govt Employee": 6,
        "Police": 6,
        "Retired": 6,
        "Teacher": 7,
        "Business Owner": 8,
        "Consultant": 8,
        "Engineer": 8,
        "Doctor": 9,
        "Professor": 9,
        "IAS": 10,
        "IPS": 10
    }
    
    
    st.title("Family Background Influence Prediction")

    gender = st.selectbox(
        "Gender",
        ["Male","Female"])
    
    
    city = st.selectbox(
        "City Type",
        list(city_map.keys())
    )
    Age = st.number_input(
        "Age",
        min_value=0,
        value=0
    )

    
    father_occ = st.selectbox(
        "Father Occupation",
        list(occupation_map.keys())
    )
    
    mother_occ = st.selectbox(
        "Mother Occupation",
        list(occupation_map.keys())
    )
    
    father_qual = st.selectbox(
        "Father Qualification",
        list(qualification_map.keys())
    )
    
    mother_qual = st.selectbox(
        "Mother Qualification",
        list(qualification_map.keys())
    )
    
    father_income = st.number_input(
        "Father Annual Income",
        min_value=0,
        value=0
    )
    
    mother_income = st.number_input(
        "Mother Annual Income",
        min_value=0,
        value=0
    )
    
    other_income = st.number_input(
        "Other Family Income",
        min_value=0,
        value=0
    )
    
    if (gender=='Male'):
        
        Gender_Female=0
        Gender_Male=1
    else:
        Gender_Female=1
        Gender_Male=0
        
    city = city_map[city]
    
    father_occ = occupation_map[father_occ]
    mother_occ = occupation_map[mother_occ]
    
    father_qual = qualification_map[father_qual]
    mother_qual = qualification_map[mother_qual]
    prediction_done = False
    
    if st.button("Predict"):
        prediction_done = True
    
        input_data = [
            Gender_Female,
            Gender_Male,
            city,
            Age,
            father_occ,
            father_qual,
            father_income,
            mother_occ,
            mother_qual,
            mother_income,
            other_income
        ]
    
        prediction = score_prediction(input_data)
        prediction_se, prediction_cse, prediction_lse = prediction
        prediction_se, prediction_cse, prediction_lse = score_prediction(input_data)

        st.session_state["pred_se"] = float(prediction_se[0])
        st.session_state["pred_cse"] = float(prediction_cse[0])
        st.session_state["pred_lse"] = float(prediction_lse[0])

        st.session_state["predicted"] = True

        st.success(f"Self-Efficacy Score : {prediction_se[0]:.2f}")
        st.success(f"Career Self-Efficacy Score : {prediction_cse[0]:.2f}")
        st.success(f"Life Self-Efficacy Score : {prediction_lse[0]:.2f}")
# Adding Questionnaire Section
        # st.markdown("---")

    if prediction_done:
        st.info(
        """
        Want to know your **actual** Self-Efficacy, Career Success Expectation and
        Life Success Expectation?

        Answer a short questionnaire and compare your actual scores with the AI prediction.
        """
        )

    if st.button("Take Questionnaire"):
        st.switch_page("pages/Questionnaire.py")
if __name__ == "__main__":
    main()
# import streamlit as st
# import joblib

# st.title("Testing Model Loading")

# try:
#     loaded_model = joblib.load("Family_trained_model.pkl")
#     st.success("✅ Model Loaded Successfully")

# except Exception as e:
#     st.error("❌ Error while loading model")
#     st.exception(e)

    