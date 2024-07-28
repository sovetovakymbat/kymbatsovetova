import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('admission_predictor_model.joblib')

# Define the feature columns
features = ['high_school_gpa', 'ent_score', 'recommendation_score', 'num_recommendations',
            'essay_score', 'keywords_count', 'num_activities', 'leadership_roles',
            'community_service_hours', 'sports_participation', 'awards_honors', 'applied_scholarships',
            'financial_aid_needed', 'family_income_level', 'submitted_on_time', 'early_application',
            'fee_paid', 'fee_waiver_granted', 'interview_conducted', 'interview_score',
            'credential_evaluation_score', 'cultural_fit_score']

# Title
st.title('Anonymous College Application')

# Create input fields for user to enter data
input_data = {}
input_data['high_school_gpa'] = st.number_input('Enter your High School GPA:', min_value=0.0, step=0.1)
input_data['ent_score'] = st.number_input('Enter your ENT Score:', min_value=0, step=1)
input_data['recommendation_score'] = st.number_input('Enter your Recommendation Score (1-5):', min_value=1, max_value=5, step=1)
input_data['num_recommendations'] = st.number_input('Enter the Number of Recommendations:', min_value=0, step=1)
input_data['essay_score'] = st.number_input('Enter your Essay Quality Score (1-10):', min_value=1, max_value=10, step=1)
input_data['keywords_count'] = st.number_input('Enter the Number of Positive Keywords in Essay:', min_value=0, step=1)
input_data['num_activities'] = st.number_input('Enter the Number of Extracurricular Activities:', min_value=0, step=1)
input_data['leadership_roles'] = st.radio('Do you have any Leadership Roles?', ('No', 'Yes'))
input_data['community_service_hours'] = st.number_input('Enter the Number of Community Service Hours:', min_value=0, step=1)
input_data['sports_participation'] = st.radio('Do you participate in Sports?', ('No', 'Yes'))
input_data['awards_honors'] = st.radio('Have you received any Awards or Honors?', ('No', 'Yes'))
input_data['applied_scholarships'] = st.radio('Have you applied for Scholarships?', ('No', 'Yes'))
input_data['financial_aid_needed'] = st.radio('Do you need Financial Aid?', ('No', 'Yes'))
input_data['family_income_level'] = st.number_input('Enter your Family Income Level:', min_value=0.0, step=1000.0)
input_data['submitted_on_time'] = st.radio('Was the Application Submitted On Time?', ('No', 'Yes'))
input_data['early_application'] = st.radio('Is this an Early Application?', ('No', 'Yes'))
input_data['fee_paid'] = st.radio('Has the Application Fee been Paid?', ('No', 'Yes'))
input_data['fee_waiver_granted'] = st.radio('Was a Fee Waiver Granted?', ('No', 'Yes'))
input_data['interview_conducted'] = st.radio('Was an Interview Conducted?', ('No', 'Yes'))
input_data['interview_score'] = st.number_input('Enter the Interview Score (1-10):', min_value=1, max_value=10, step=1)
input_data['credential_evaluation_score'] = st.number_input('Enter the Credential Evaluation Score (1-5):', min_value=1, max_value=5, step=1)
input_data['cultural_fit_score'] = st.number_input('Enter the Cultural Fit Score (1-5):', min_value=1, max_value=5, step=1)

# Convert categorical variables to numerical
input_data['leadership_roles'] = 1 if input_data['leadership_roles'] == 'Yes' else 0
input_data['sports_participation'] = 1 if input_data['sports_participation'] == 'Yes' else 0
input_data['awards_honors'] = 1 if input_data['awards_honors'] == 'Yes' else 0
input_data['applied_scholarships'] = 1 if input_data['applied_scholarships'] == 'Yes' else 0
input_data['financial_aid_needed'] = 1 if input_data['financial_aid_needed'] == 'Yes' else 0
input_data['submitted_on_time'] = 1 if input_data['submitted_on_time'] == 'Yes' else 0
input_data['early_application'] = 1 if input_data['early_application'] == 'Yes' else 0
input_data['fee_paid'] = 1 if input_data['fee_paid'] == 'Yes' else 0
input_data['fee_waiver_granted'] = 1 if input_data['fee_waiver_granted'] == 'Yes' else 0
input_data['interview_conducted'] = 1 if input_data['interview_conducted'] == 'Yes' else 0

# Create a DataFrame from the user input
input_df = pd.DataFrame([input_data])

# Display user input for confirmation
st.write('User Input:')
st.write(input_df)

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.success('The student is predicted to be admitted!')
    else:
        st.warning('The student is predicted to not be admitted.')
