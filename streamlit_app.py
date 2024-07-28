import streamlit as st

# Title
st.title('Anonymous College Application')

# High School GPA
gpa = st.number_input('Enter your High School GPA:')
st.write(f'High School GPA: {gpa}')

# Unified National Test (ENT) Score
ent_score = st.number_input('Enter your ENT Score:')
st.write(f'ENT Score: {ent_score}')

# Recommendation Score
recommendation_score = st.number_input('Enter your Recommendation Score (1-5):')
st.write(f'Recommendation Score: {recommendation_score}')

# Number of Recommendations
num_recommendations = st.number_input('Enter the Number of Recommendations:', min_value=0, step=1)
st.write(f'Number of Recommendations: {num_recommendations}')

# Essay Quality Score
essay_score = st.number_input('Enter your Essay Quality Score (1-10):')
st.write(f'Essay Quality Score: {essay_score}')

# Keywords Count in Essay
keywords_count = st.number_input('Enter the Number of Positive Keywords in Essay:')
st.write(f'Keywords Count in Essay: {keywords_count}')

# Number of Extracurricular Activities
num_activities = st.number_input('Enter the Number of Extracurricular Activities:', min_value=0, step=1)
st.write(f'Number of Extracurricular Activities: {num_activities}')

# Leadership Roles
leadership_roles = st.radio('Do you have any Leadership Roles?', ('No', 'Yes'))
st.write(f'Leadership Roles: {1 if leadership_roles == "Yes" else 0}')

# Community Service Hours
community_service_hours = st.number_input('Enter the Number of Community Service Hours:')
st.write(f'Community Service Hours: {community_service_hours}')

# Sports Participation
sports_participation = st.radio('Do you participate in Sports?', ('No', 'Yes'))
st.write(f'Sports Participation: {1 if sports_participation == "Yes" else 0}')

# Awards and Honors
awards_honors = st.radio('Have you received any Awards or Honors?', ('No', 'Yes'))
st.write(f'Awards and Honors: {1 if awards_honors == "Yes" else 0}')

# Applied for Scholarships
applied_scholarships = st.radio('Have you applied for Scholarships?', ('No', 'Yes'))
st.write(f'Applied for Scholarships: {1 if applied_scholarships == "Yes" else 0}')

# Financial Aid Needed
financial_aid_needed = st.radio('Do you need Financial Aid?', ('No', 'Yes'))
st.write(f'Financial Aid Needed: {1 if financial_aid_needed == "Yes" else 0}')

# Family Income Level
family_income_level = st.number_input('Enter your Family Income Level:')
st.write(f'Family Income Level: {family_income_level}')

# Application Submitted On Time
submitted_on_time = st.radio('Was the Application Submitted On Time?', ('No', 'Yes'))
st.write(f'Application Submitted On Time: {1 if submitted_on_time == "Yes" else 0}')

# Early Application
early_application = st.radio('Is this an Early Application?', ('No', 'Yes'))
st.write(f'Early Application: {1 if early_application == "Yes" else 0}')

# Application Fee Paid
fee_paid = st.radio('Has the Application Fee been Paid?', ('No', 'Yes'))
st.write(f'Fee Paid: {1 if fee_paid == "Yes" else 0}')

# Fee Waiver Granted
fee_waiver_granted = st.radio('Was a Fee Waiver Granted?', ('No', 'Yes'))
st.write(f'Fee Waiver Granted: {1 if fee_waiver_granted == "Yes" else 0}')

# Interview Conducted
interview_conducted = st.radio('Was an Interview Conducted?', ('No', 'Yes'))
st.write(f'Interview Conducted: {1 if interview_conducted == "Yes" else 0}')

# Interview Score
interview_score = st.number_input('Enter the Interview Score (1-10):')
st.write(f'Interview Score: {interview_score}')

# Credential Evaluation Score
credential_evaluation_score = st.number_input('Enter the Credential Evaluation Score (1-5):')
st.write(f'Credential Evaluation Score: {credential_evaluation_score}')

# Cultural Fit Score
cultural_fit_score = st.number_input('Enter the Cultural Fit Score (1-5):')
st.write(f'Cultural Fit Score: {cultural_fit_score}')
