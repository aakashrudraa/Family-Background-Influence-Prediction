import streamlit as st

options = [
    "1 - Strongly Disagree",
    "2 - Disagree",
    "3 - Neutral",
    "4 - Agree",
    "5 - Strongly Agree"
]
st.header("Self-Efficacy Assessment")

se1 = st.slider("1. I can solve difficult problems if I try hard enough.", 1, 5, 3)
se2 = st.slider("2. I remain confident even when facing unexpected challenges.", 1, 5, 3)
se3 = st.slider("3. I can learn new skills when I put in sufficient effort.", 1, 5, 3)
se4 = st.slider("4. I believe I can achieve the goals I set for myself.", 1, 5, 3)
se5 = st.slider("5. I can handle stressful situations effectively.", 1, 5, 3)
se6 = st.slider("6. I recover quickly after setbacks or failures.", 1, 5, 3)
se7 = st.slider("7. I can make good decisions even under pressure.", 1, 5, 3)
se8 = st.slider("8. I believe I can overcome obstacles through persistence.", 1, 5, 3)
se9 = st.slider("9. I am confident in completing tasks that are important to me.", 1, 5, 3)
se10 = st.slider("10. I believe I can succeed even when others doubt me.", 1, 5, 3)


st.header("Career Success Expectation")

cse1 = st.slider("1. I expect to achieve a successful career.", 1, 5, 3)
cse2 = st.slider("2. I believe I will obtain a job that matches my abilities.", 1, 5, 3)
cse3 = st.slider("3. I expect to achieve financial stability through my career.", 1, 5, 3)
cse4 = st.slider("4. I believe my future work will be meaningful.", 1, 5, 3)
cse5 = st.slider("5. I expect to be recognized for my professional achievements.", 1, 5, 3)
cse6 = st.slider("6. I believe I can reach leadership positions in my career.", 1, 5, 3)
cse7 = st.slider("7. I expect to continue learning and growing professionally.", 1, 5, 3)
cse8 = st.slider("8. I believe I can overcome career-related challenges.", 1, 5, 3)
cse9 = st.slider("9. I am optimistic about achieving my long-term career goals.", 1, 5, 3)
cse10 = st.slider("10. I believe my efforts today will contribute to future career success.", 1, 5, 3)


st.header("Life Success Expectation")

lse1 = st.slider("1. I expect to lead a satisfying life.", 1, 5, 3)
lse2 = st.slider("2. I believe I will achieve my personal life goals.", 1, 5, 3)
lse3 = st.slider("3. I expect to maintain healthy relationships throughout life.", 1, 5, 3)
lse4 = st.slider("4. I believe I will achieve financial security.", 1, 5, 3)
lse5 = st.slider("5. I expect to maintain a healthy work-life balance.", 1, 5, 3)
lse6 = st.slider("6. I believe I will positively contribute to society.", 1, 5, 3)
lse7 = st.slider("7. I expect to overcome major life difficulties successfully.", 1, 5, 3)
lse8 = st.slider("8. I believe I will be satisfied with my life in the future.", 1, 5, 3)
lse9 = st.slider("9. I expect to achieve a balance between personal and professional success.", 1, 5, 3)
lse10 = st.slider("10. I believe I have the ability to build the future I desire.", 1, 5, 3)

if st.button("Calculate My Scores"):

    se_total = sum([se1, se2, se3, se4, se5, se6, se7, se8, se9, se10])

    cse_total = sum([cse1, cse2, cse3, cse4, cse5,
                     cse6, cse7, cse8, cse9, cse10])

    lse_total = sum([lse1, lse2, lse3, lse4, lse5,
                     lse6, lse7, lse8, lse9, lse10])
    
    st.session_state["actual_se"] = se_total
    st.session_state["actual_cse"] = cse_total
    st.session_state["actual_lse"] = lse_total

    st.session_state["questionnaire_done"] = True

    st.success(f"Self-Efficacy Score: {se_total}")
    st.success(f"Career Success Expectation Score: {cse_total}")
    st.success(f"Life Success Expectation Score: {lse_total}")


    if st.session_state.get("questionnaire_done", False):

        st.header("Prediction vs Actual")

        comparison = {
            "Score":[
                "Self-Efficacy",
                "Career Success",
                "Life Success"
            ],
            "Predicted":[
                st.session_state["pred_se"],
                st.session_state["pred_cse"],
                st.session_state["pred_lse"]
            ],
            "Actual":[
                st.session_state["actual_se"],
                st.session_state["actual_cse"],
                st.session_state["actual_lse"]
            ]
        }

        st.table(comparison)
        comparison["Difference"] = [
    abs(st.session_state["pred_se"]-st.session_state["actual_se"]),
    abs(st.session_state["pred_cse"]-st.session_state["actual_cse"]),
    abs(st.session_state["pred_lse"]-st.session_state["actual_lse"])]
