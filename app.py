import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("insurance_model.pkl", "rb"))

# Title
st.title(" Medical Insurance Cost Prediction")

st.write("Enter the patient details below.")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)

sex = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=28.5
)

children = st.selectbox(
    "Number of Children",
    [0,1,2,3,4,5]
)

smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
)

region = st.selectbox(
    "Region",
    ["Southwest","Southeast","Northwest","Northeast"]
)

# Encoding

sex = 1 if sex == "Male" else 0

smoker = 1 if smoker == "Yes" else 0

region_dict = {
    "Northeast":0,
    "Northwest":1,
    "Southeast":2,
    "Southwest":3
}

region = region_dict[region]

# Create DataFrame

input_data = pd.DataFrame({
    "age":[age],
    "sex":[sex],
    "bmi":[bmi],
    "children":[children],
    "smoker":[smoker],
    "region":[region]
})

# Prediction

if st.button("Predict Insurance Charge"):

    prediction = model.predict(input_data)

    st.success(f"Predicted Insurance Charge: ₹{prediction[0]:,.0f}")