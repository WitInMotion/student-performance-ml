
import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("student_model.pkl", "rb"))

st.title("🎓 Student Grade Predictor")

st.write("Enter the student information below:")

hours = st.number_input("Hours Studied", min_value=0.0)
attendance = st.number_input("Attendance (%)", min_value=0.0)
previous_grade = st.number_input("Previous Grade", min_value=0.0)

if st.button("Predict Final Grade"):

    features = np.array([[hours, attendance, previous_grade]])
    prediction = model.predict(features)

    st.success(f"Predicted Final Grade: {prediction[0]:.2f}")
