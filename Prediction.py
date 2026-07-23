
import numpy as np
import joblib
import streamlit as st

loaded_model = joblib.load("Family_trained_model.pkl")

if "pred_se" not in st.session_state:
    st.session_state["pred_se"] = None

if "pred_cse" not in st.session_state:
    st.session_state["pred_cse"] = None

if "pred_lse" not in st.session_state:
    st.session_state["pred_lse"] = None

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

        st.session_state["pred_se"] = float(prediction_se[0])
        st.session_state["pred_cse"] = float(prediction_cse[0])
        st.session_state["pred_lse"] = float(prediction_lse[0])

        st.session_state["predicted"] = True

        st.markdown("---")
        st.subheader("Understanding the Predicted Scores")

        st.markdown("""
        ### 🔹 Self-Efficacy (SE)
        Self-Efficacy refers to an individual's belief in their ability to successfully perform tasks, overcome challenges, and achieve goals. A higher score indicates greater confidence in handling difficult situations and accomplishing objectives.

        ### 🔹 Career Success Expectation (CSE)
        Career Success Expectation reflects how positively an individual views their future career prospects. A higher score suggests stronger confidence in achieving career growth, professional success, and long-term career aspirations.

        ### 🔹 Life Success Expectation (LSE)
        Life Success Expectation measures an individual's optimism about achieving important life goals and leading a fulfilling life. A higher score indicates greater confidence in attaining personal, financial, and social success in the future.
        """)

        st.info("""
        **Note:** The predicted scores are generated using a machine learning model trained on historical data. These predictions reflect statistical patterns learned from the dataset and should be interpreted as informative estimates rather than definitive measures of an individual's abilities, personality, or future outcomes.
        """)
        st.markdown("---")

        st.success(f"Self-Efficacy Score : {prediction_se[0]:.2f}")
        if prediction_se[0] < 29:
            st.warning("Your Self-Efficacy score is low. Consider seeking support or resources to improve your self-efficacy. You may underestimate your abilities or feel less confident when facing challenges. Developing skills gradually and gaining successful experiences can help improve self-confidence.")
        elif prediction_se[0] < 36:
            st.info("Your Self-Efficacy score is moderate. You have a reasonable level of self-efficacy, but there may be areas where you can further enhance your confidence and belief in your abilities. Consider setting achievable goals and seeking opportunities for skill development to strengthen your self-efficacy. You generally believe in your abilities but may hesitate in unfamiliar or difficult situations.")
        else:
            st.success("Your Self-Efficacy score is high. You have a strong belief in your abilities and are likely to approach challenges with confidence. Your high self-efficacy can contribute to better performance and resilience in various aspects of life. Keep leveraging your strengths and continue to build on your successes.")



        st.success(f"Career Self-Efficacy Score : {prediction_cse[0]:.2f}")
        if prediction_cse[0] < 29:
            st.warning("Your Career Self-Efficacy score is low. You may feel uncertain about your future career path or opportunities. Career guidance and skill development can help improve confidence.")
        elif prediction_cse[0] < 36:
            st.info("Your Career Self-Efficacy score is moderate. You have a reasonable level of career self-efficacy, You have balanced expectations. Building career skills, networking, and gaining practical experience may strengthen your confidence.")
        else:
            st.success("Your Career Self-Efficacy score is high. You have a strong belief in your career abilities and are likely to approach challenges with confidence. Your high career self-efficacy can contribute to better performance and resilience in various aspects of life. Keep leveraging your strengths and continue to build on your successes.")



        st.success(f"Life Self-Efficacy Score : {prediction_lse[0]:.2f}")
        if prediction_lse[0] < 29:
            st.warning("Your Life Self-Efficacy score is low. You may have doubts about achieving long-term goals. Setting realistic milestones and celebrating progress can improve your outlook.")
        elif prediction_lse[0] < 36:
            st.info("Your Life Self-Efficacy score is moderate. You have a reasonable level of life self-efficacy, You have moderate optimism regarding future life achievements, with room for greater confidence. Consider setting achievable goals and seeking opportunities for skill development to strengthen your life self-efficacy. You generally have a positive outlook toward achieving your long-term personal and life goals, but may experience some doubts or uncertainties.")
        else:
            st.success("Your Life Self-Efficacy score is high. You generally have a positive outlook toward achieving your long-term personal and life goals.")

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
