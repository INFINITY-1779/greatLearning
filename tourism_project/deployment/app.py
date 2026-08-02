import os
import streamlit as st
import pandas as pd
import joblib

# Load the model committed by the pipeline (sits next to this file)
model_path = os.path.join(os.path.dirname(__file__), "best_tourism_model.joblib")
model = joblib.load(model_path)

st.title("Tourism Product Buying Prediction App")
st.write("""
predicts whether a customer will purchase the newly introduced Wellness Tourism Package before contacting them.
""")

age = st.sidebar.slider('Age', 18, 70, 30)
typeofcontact = st.sidebar.selectbox('Type of Contact', ('Company Invited', 'Self Inquiry'))
citytier = st.sidebar.selectbox('City Tier', (1, 2, 3))
occupation = st.sidebar.selectbox('Occupation', ('Salaried', 'Small Business', 'Large Business', 'Free Lancer'))
gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
numberofpersonvisiting = st.sidebar.slider('Number of Persons Visiting', 1, 6, 2)
preferredpropertystar = st.sidebar.selectbox('Preferred Property Star', (3, 4, 5))
maritalstatus = st.sidebar.selectbox('Marital Status', ('Married', 'Single', 'Divorced'))
numberoftrips = st.sidebar.slider('Number of Trips Annually', 1, 10, 3)
passport = st.sidebar.selectbox('Passport', (0, 1), format_func=lambda x: 'Yes' if x==1 else 'No')
owncar = st.sidebar.selectbox('Own Car', (0, 1), format_func=lambda x: 'Yes' if x==1 else 'No')
numberofchildrenvisiting = st.sidebar.slider('Number of Children Visiting (under 5)', 0, 4, 0)
designation = st.sidebar.selectbox('Designation', (
            'Executive', 'Manager', 'Senior Manager', 'AVP', 'VP', 'Director', 'Junior Executive', 'President'
        ))
monthlyincome = st.sidebar.slider('Monthly Income', 10000, 100000, 30000)
pitchsatisfactionsore = st.sidebar.slider('Pitch Satisfaction Score', 1, 5, 3)
productpitched = st.sidebar.selectbox('Product Pitched', (
            'Luxury', 'Deluxe', 'Standard', 'Super Deluxe', 'Basic', 'King'
        ))
numberoffollowups = st.sidebar.slider('Number of Follow-ups', 1, 6, 3)

input_data = pd.DataFrame({
    'Age': age,
    'TypeofContact': typeofcontact,
    'CityTier': citytier,
    'Occupation': occupation,
    'Gender': gender,
    'NumberOfPersonVisiting': numberofpersonvisiting,
    'PreferredPropertyStar': preferredpropertystar,
    'MaritalStatus': maritalstatus,
    'NumberOfTrips': numberoftrips,
    'Passport': passport,
    'OwnCar': owncar,
    'NumberOfChildrenVisiting': numberofchildrenvisiting,
    'Designation': designation,
    'MonthlyIncome': monthlyincome,
    'PitchSatisfactionScore': pitchsatisfactionsore,
    'ProductPitched': productpitched,
    'NumberOfFollowups': numberoffollowups
    })

if st.button("Tourism Purchase"):
    prediction = model.predict(input_data)[0]
    result = "Tourism Purchase Likely" if prediction == 1 else "Tourism Purchase Unlikely"
    st.subheader("Prediction Result:")
    st.success(f"The model predicts: **{result}**")
