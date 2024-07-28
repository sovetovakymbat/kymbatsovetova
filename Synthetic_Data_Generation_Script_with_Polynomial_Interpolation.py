import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

def generate_synthetic_data(num_samples=1000):
    np.random.seed(42)
    
    # Generate base data
    high_school_gpa = np.round(np.random.uniform(2.0, 4.0, num_samples), 2)
    ent_score = np.random.randint(50, 100, num_samples)
    recommendation_score = np.random.randint(1, 6, num_samples)
    num_recommendations = np.random.randint(0, 5, num_samples)
    essay_score = np.random.randint(1, 11, num_samples)
    keywords_count = np.random.randint(0, 20, num_samples)
    num_activities = np.random.randint(0, 10, num_samples)
    leadership_roles = np.random.randint(0, 2, num_samples)
    community_service_hours = np.random.randint(0, 200, num_samples)
    sports_participation = np.random.randint(0, 2, num_samples)
    awards_honors = np.random.randint(0, 2, num_samples)
    applied_scholarships = np.random.randint(0, 2, num_samples)
    financial_aid_needed = np.random.randint(0, 2, num_samples)
    family_income_level = np.random.uniform(20000, 150000, num_samples)
    submitted_on_time = np.random.randint(0, 2, num_samples)
    early_application = np.random.randint(0, 2, num_samples)
    fee_paid = np.random.randint(0, 2, num_samples)
    fee_waiver_granted = np.random.randint(0, 2, num_samples)
    interview_conducted = np.random.randint(0, 2, num_samples)
    interview_score = np.random.randint(1, 11, num_samples)
    credential_evaluation_score = np.random.randint(1, 6, num_samples)
    cultural_fit_score = np.random.randint(1, 6, num_samples)
    admitted = np.random.randint(0, 2, num_samples)

    # Combine into a DataFrame
    data = {
        'high_school_gpa': high_school_gpa,
        'ent_score': ent_score,
        'recommendation_score': recommendation_score,
        'num_recommendations': num_recommendations,
        'essay_score': essay_score,
        'keywords_count': keywords_count,
        'num_activities': num_activities,
        'leadership_roles': leadership_roles,
        'community_service_hours': community_service_hours,
        'sports_participation': sports_participation,
        'awards_honors': awards_honors,
        'applied_scholarships': applied_scholarships,
        'financial_aid_needed': financial_aid_needed,
        'family_income_level': family_income_level,
        'submitted_on_time': submitted_on_time,
        'early_application': early_application,
        'fee_paid': fee_paid,
        'fee_waiver_granted': fee_waiver_granted,
        'interview_conducted': interview_conducted,
        'interview_score': interview_score,
        'credential_evaluation_score': credential_evaluation_score,
        'cultural_fit_score': cultural_fit_score,
        'admitted': admitted
    }

    df = pd.DataFrame(data)
    
    # Apply polynomial interpolation to add synthetic complexity
    poly = PolynomialFeatures(degree=2, include_bias=False)
    poly_features = poly.fit_transform(df.drop('admitted', axis=1))
    poly_feature_names = poly.get_feature_names_out(df.columns[:-1])
    df_poly = pd.DataFrame(poly_features, columns=poly_feature_names)
    
    # Add the target variable back
    df_poly['admitted'] = df['admitted']
    
    # Save to CSV in the same repository
    df_poly.to_csv('data.csv', index=False)
    print("Synthetic data generated and saved to 'data.csv'")

if __name__ == "__main__":
    generate_synthetic_data()
