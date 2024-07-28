import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
# Assume 'data.csv' is in the same directory and contains the relevant data
data = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print(data.head())

# Define the feature columns and the target column
# Example: Let's assume 'admitted' is the target column indicating acceptance (1 for accepted, 0 for not accepted)
features = ['high_school_gpa', 'ent_score', 'recommendation_score', 'num_recommendations',
            'essay_score', 'keywords_count', 'num_activities', 'leadership_roles',
            'community_service_hours', 'sports_participation', 'awards_honors', 'applied_scholarships',
            'financial_aid_needed', 'family_income_level', 'submitted_on_time', 'early_application',
            'fee_paid', 'fee_waiver_granted', 'interview_conducted', 'interview_score',
            'credential_evaluation_score', 'cultural_fit_score']
target = 'admitted'

# Preprocess data
X = data[features]
y = data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)

# Save the model for later use
import joblib
joblib.dump(model, 'admission_predictor_model.joblib')


