import pandas as pd
import streamlit as st
import pickle
import os
from model import MODEL_PATH
from sklearn.preprocessing import MinMaxScaler



#load_dotenv()
#model_path = os.getenv("MODEL_PATH")
#with open(model_path, 'rb') as model_file:
    #model = pickle.load(model_file)

# Load the model
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app title and description
st.markdown("""
# **PredictDiabetes 🍩**  
### Early Screening Tool for Type 2 Diabetes Mellitus 
""")
st.write('An easy-to-use web app designed to assess the risk of Type 2 Diabetes using personalized input features')

st.write('*__1 - DEMOGRAPHIC VALUES__*')
# Gender Mapping
gender_mapping = {
    "Female": 0,
    "Male": 1
}

# Gender Selectbox
gender = st.selectbox(
    'Gender:',
    list(gender_mapping.keys())
)
# Map the selected gender string to the corresponding number
gender_value = gender_mapping[gender]
#st.write(f"Selected Gender: {gender} (Mapped Value: {gender_value})")

#age
age = st.number_input(
    'Enter your age:',
    min_value=0,  # Minimum age
    max_value=120,  # Maximum age
    value=25  # Default value
)
#st.write(f"Entered Age: {age}")

# Education Level Mapping
education_mapping = {
    "No formal schooling": 0,
    "Lower secondary education": 1,
    "Pre-university education": 2,
    "Upper secondary education": 3,
    "Primary education": 4,
    "Master's degree": 5,
    "Diploma from college/polytechnic/university": 6,
    "Pre-primary education": 7,
    "Bachelor's degree/postgraduate diploma": 8,
    "Certificate from college/polytechnic/university": 9,
    "Doctoral degree/fellowship": 10
}

# Education Level Selectbox
education_level = st.selectbox(
    'Education Level:',
    list(education_mapping.keys())
)
# Map the selected education level string to the corresponding number
education_level_value = education_mapping[education_level]
#st.write(f"Selected Education Level: {education_level} (Mapped Value: {education_level_value})")

# Races Group Mapping
races_mapping = {
    "Malay": 0,
    "Indian": 1,
    "Chinese": 2,
    "Indigenous Sarawak": 3,
    "Other": 4,
    "Indigenous Sabah": 5,
    "Orang Asli (Peninsular)": 6
}

# Races Group Selectbox
races_group = st.selectbox(
    'Races Group:',
    list(races_mapping.keys())
)
# Map the selected race group string to the corresponding number
races_group_value = races_mapping[races_group]
#st.write(f"Selected Race Group: {races_group} (Mapped Value: {races_group_value})")

# Marital Status Mapping
marital_status_mapping = {
    "Married": 0,
    "Never married": 1,
    "Divorced": 2,
    "Single": 3
}

# Marital Status Selectbox
maritial_status = st.selectbox(
    'Marital Status:',
    list(marital_status_mapping.keys())
)
# Map the selected marital status string to the corresponding number
maritial_status_value = marital_status_mapping[maritial_status]
#st.write(f"Selected Marital Status: {maritial_status} (Mapped Value: {maritial_status_value})")

# Work Status Mapping
work_status_mapping = {
    "Retired": 0,
    "Unemployed (unable to work)": 1,
    "Homemaker": 2,
    "Unemployed (able to work)": 3,
    "Self-employed": 4,
    "Private company employee": 5,
    "Semi-government (statutory board) employee": 6,
    "Government employee": 7,
    "Non-paid": 8,
    "Student": 9
}

# Work Status Selectbox
work_status = st.selectbox(
    'Work Status:',
    list(work_status_mapping.keys())
)
# Map the selected work status string to the corresponding number
work_status_value = work_status_mapping[work_status]
#st.write(f"Selected Work Status: {work_status} (Mapped Value: {work_status_value})")

# Religion Mapping
religion_mapping = {
    "Islam": 0,
    "Hindu": 1,
    "Buddha": 2,
    "Sikhism": 3,
    "Christian": 4,
    "No religion": 5,
    "Taoism": 6,
    "Other": 7
}

# Religion Selectbox
religion = st.selectbox(
    'Religion:',
    list(religion_mapping.keys())
)
# Map the selected religion string to the corresponding number
religion_value = religion_mapping[religion]
#st.write(f"Selected Religion: {religion} (Mapped Value: {religion_value})")


# Physical measurements
st.write('*__2 - PHYSICAL EXAMINATION__*')
height_cm = st.number_input("Height (cm) 📏", min_value=50.0, max_value=250.0, value=165.0, step=0.1)
height = height_cm / 100
weight = st.number_input("Weight (kg) ⚖️", min_value=20.0, max_value=200.0, value=70.0, step=0.1)
# Calculate BMI
bmi = weight / (height ** 2)
# Display the BMI result
st.write(f"Your BMI is: {bmi:.2f}") 
bp_syst = st.number_input("Systolic Blood Pressure (bp_syst) 💓", min_value=50, max_value=250, value=120)
bp_diast = st.number_input("Diastolic Blood Pressure (bp_diast) 💓", min_value=30, max_value=150, value=80)

# Health conditions (binary inputs)
st.write('*__3 - MEDICAL HISTORY__*')
# Define option mappings
options_map = {"No": 0, "Yes": 1}

personal_chd = options_map[st.selectbox("Do you have any personal history of CHD (Coronary Heart Disease)", options=list(options_map.keys()), index=0)]
personal_stroke = options_map[st.selectbox("Do you have any personal history of Stroke", options=list(options_map.keys()), index=0)]
personal_ckd = options_map[st.selectbox("Do you have any personal history of CKD (Chronic Kidney Disease)", options=list(options_map.keys()), index=0)]
personal_asthma = options_map[st.selectbox("Do you have any personal history of Asthma", options=list(options_map.keys()), index=0)]
personal_others = options_map[st.selectbox("Do you have any other personal health conditions", options=list(options_map.keys()), index=0)]
personal_dm = options_map[st.selectbox("Do you have any personal history of Diabetes Mellitus", options=list(options_map.keys()), index=0)]
personal_htn = options_map[st.selectbox("Do you have any personal history of Hypertension", options=list(options_map.keys()), index=0)]
personal_hcl = options_map[st.selectbox("Do you have any personal history of High Cholesterol", options=list(options_map.keys()), index=0)]

# Demographic and lifestyle factors
st.write('*__4 - BEHAVIOURAL RISK__*')
smoking = options_map[st.selectbox("Are you a smoker?", options=list(options_map.keys()), index=0)]
#smoking = st.selectbox("Smoking Status 🚭", options=[0, 1], index=0)  # 0: Non-Smoker, 1: Smoker
#physical_activity = st.selectbox("Physical Activity Level 💪", options=[0, 1, 2], index=0)  # 0: None, 1: Moderate, 2: Vigorous

# MET (Metabolic Equivalent of Task)
st.write('*__5 - PHYSICAL ACTIVITY__*')

st.markdown('**_5.1 Vigorous Activity_**')
# Ask for the number of days per week for vigorous activity
vigorous_activity_days = st.number_input("How many days per week do you engage in vigorous activity for AT LEAST 10 MINUTES CONTINUOUSLY?", min_value=0, max_value=7, value=0)

# Side-by-side input for hours and minutes
col1, col2 = st.columns(2)
with col1:
    vigorous_activity_hours = st.number_input("Hours per day (vigorous activity)", min_value=0, max_value=24, value=0, key="vigorous_hours")
with col2:
    vigorous_activity_minutes = st.number_input("Minutes per day (vigorous activity)", min_value=0, max_value=60, value=0, key="vigorous_minutes")

st.markdown('**_5.2 Moderate Activity_**')
# Ask for the number of days per week for moderate activity
moderate_activity_days = st.number_input("How many days per week do you do moderate-intensity activities for AT LEAST 10 MINUTES CONTINUOUSLY?", min_value=0, max_value=7, value=0)

# Side-by-side input for hours and minutes
col3, col4 = st.columns(2)
with col3:
    moderate_activity_hours = st.number_input("Hours per day (moderate activity) ", min_value=0, max_value=24, value=0, key="moderate_hours")
with col4:
    moderate_activity_minutes = st.number_input("Minutes per day (moderate activity)", min_value=0, max_value=60, value=0, key="moderate_minutes")

st.markdown('**_5.3 Walking Activity_**')
# Ask for the number of days per week for walk activity
walk_activity_days = st.number_input("How many days per week do you walk for AT LEAST 10 MINUTES CONTINUOUSLY?", min_value=0, max_value=7, value=0)

# Side-by-side input for hours and minutes
col5, col6 = st.columns(2)
with col5:
    walk_activity_hours = st.number_input("Hours per day (walking activity)", min_value=0, max_value=24, value=0, key="walk_hours")
with col6:
    walk_activity_minutes = st.number_input("Minutes per day (walking activity)", min_value=0, max_value=60, value=0, key="walk_minutes")


# Ask for the number of hours and minutes per day for moderate activity
#walk_activity_hours = st.number_input("How many hours do you spend walking on one of those days?", min_value=0, max_value=24, value=0)
#walk_activity_minutes = st.number_input("How many minutes do you spend walking on one of those days?", min_value=0, max_value=60, value=0)

#Calculate
st.markdown('**_5.4 Total METminutes_**')
#METvig
vigorous_hourmin = (vigorous_activity_hours * 60) + vigorous_activity_minutes
METvig = vigorous_hourmin * vigorous_activity_days * 8

#METmod
moderate_hourmin = (moderate_activity_hours * 60) + moderate_activity_minutes
METmod = moderate_hourmin * moderate_activity_days * 4


#METwalk
walk_hourmin = (walk_activity_hours * 60) + walk_activity_minutes
METwalk = walk_hourmin * walk_activity_days * 3.3

METminutes = METvig + METmod + METwalk
st.write(METminutes)

# physical_activity
st.markdown('**_5.5 Physical Activities_**')
VMW_comb_day = vigorous_activity_days + moderate_activity_days + walk_activity_days
MW_comb_day = moderate_activity_days + walk_activity_days

# Activity Level Classification
physical_activity = 1  # Default to "Low"
if (vigorous_activity_days >= 3 and METminutes >= 1500) or (VMW_comb_day >= 7 and METminutes >= 3000):
    physical_activity = 3  # High
elif (vigorous_activity_days >= 3 or (vigorous_activity_days >= 7 and vigorous_hourmin >= 30)) or \
     (moderate_activity_days >= 5 or (walk_activity_days >= 7 and walk_hourmin >= 30)) or \
     (VMW_comb_day >= 5 and METminutes >= 600):
    physical_activity = 2  # Moderate

# Mapping activity level to label
physical_activity_mapping = {1: "Low", 2: "Moderate", 3: "High"}
physical_activity_label = physical_activity_mapping[physical_activity]

# Display the result
st.write(physical_activity_label)

# Display input data (optional)
if st.button("Submit 📝"):
    st.write({
        "personal_chd": personal_chd,
        "personal_stroke": personal_stroke,
        "personal_ckd": personal_ckd,
        "personal_asthma": personal_asthma,
        "personal_others": personal_others,
        "personal_dm": personal_dm,
        "personal_htn": personal_htn,
        "personal_hcl": personal_hcl,
        "height": height,
        "weight": weight,
        "bp_syst": bp_syst,
        "bp_diast": bp_diast,
        "gender_id": gender_value,
        "smoking": smoking,
        "physical_activity": physical_activity,
        "bmi": bmi,
        "METvig": METvig,
        "METmod": METmod,
        "METwalk": METwalk,
        "METminutes": METminutes,
        "education_level": education_level_value,
        "races_group": races_group_value,
        "maritial_status": maritial_status_value,
        "work_status": work_status_value,
        "religion": religion_value,
    })

# Create a dictionary of the user input features
data = {
     "personal_chd": personal_chd,
        "personal_stroke": personal_stroke,
        "personal_ckd": personal_ckd,
        "personal_asthma": personal_asthma,
        "personal_others": personal_others,
        "personal_dm": personal_dm,
        "personal_htn": personal_htn,
        "personal_hcl": personal_hcl,
        "height": height,
        "weight": weight,
        "bp_syst": bp_syst,
        "bp_diast": bp_diast,
        "gender_id": gender_value,
        "member_age20":age,
        "smoking": smoking,
        "physical_activity": physical_activity,
        "bmi": bmi,
        "METvig": METvig,
        "METmod": METmod,
        "METwalk": METwalk,
        "METminutes": METminutes,
        "education_level": education_level_value,
        "races_group": races_group_value,
        "maritial_status": maritial_status_value,
        "work_status": work_status_value,
        "religion": religion_value,
}

rf_model = model['model']  # Extract the RandomForest model
scaler = model['scaler']   # Extract the scaler (if needed)

# Convert the data dictionary into a DataFrame
features = pd.DataFrame(data, index=[0])

user_features_scaled = scaler.transform(features)

# Preprocess input data
#scaler.fit(features)
#user_features_scaled = scaler.transform(features)

# Make prediction
prediction = rf_model.predict_proba(user_features_scaled)


# RESULT
st.write('*__6 - PREDICTION RESULT__*')

# Ensure that prediction is properly processed
if prediction.ndim > 1 and prediction.shape[1] > 1:
    Probability_percentage = prediction[0][1] * 100  # Probability of the positive class in percentage
    
    # Check the threshold for 'Yes' or 'No' prediction
    if prediction[0][1] >= 0.5:  # Assuming threshold of 0.5
        st.markdown(
            f"""
            **<span style='background-color: yellow;'>Predicted DM Status:</span>** <span style='font-size: 18px; font-weight: bold; color: black;'>Yes</span><br>
            **<span style='background-color: yellow;'>Probability_percentage:</span>** <span style='font-size: 18px; font-weight: bold; color: black;'>{Probability_percentage:.0f}%</span>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            **<span style='background-color: yellow;'>Predicted DM Status:</span>** <span style='font-size: 18px; font-weight: bold; color: red;'>No</span><br>
            **<span style='background-color: yellow;'>Probability_percentage:</span>** <span style='font-size: 18px; font-weight: bold; color: red;'>{Probability_percentage:.0f}%</span>
            """,
            unsafe_allow_html=True
        )

st.write('_*Disclaimer - The above result is only a prediction using non laboratory data. Please visit a nearby GP or KK for a comprehensive health screening and accurate diagnosis._')

st.write('Healthcare Technology and Innovation Unit © ProtectHealth 2025.')
