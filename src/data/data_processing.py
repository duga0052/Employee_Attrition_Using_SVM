import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.feature.build_features import create_dummy_variables, map_binary_columns, engineer_features
import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname=s - %(message)s')

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info("Data loaded successfully from %s", file_path)
        
            # Display the first few rows of the dataframe
        print("First few rows of the dataframe:")
        print(df.sample(5))

        print("\nDataframe information:")
        # Display information about the dataframe
        df.info()
    
        return df
    except Exception as e:
        logging.error("Error loading data: %s", e)
        raise

def preprocess_data(df):
    try:
        df = df.drop(['EmployeeNumber', 'Over18', 'StandardHours'], axis=1)
        logging.info("Dropped unnecessary columns")

        num_cols = ['DailyRate', 'Age', 'DistanceFromHome', 'MonthlyIncome', 'MonthlyRate', 'PercentSalaryHike', 'TotalWorkingYears',
                    'YearsAtCompany', 'NumCompaniesWorked', 'HourlyRate', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'TrainingTimesLastYear']
        cat_cols = ['Attrition', 'OverTime', 'BusinessTravel', 'Department', 'Education', 'EducationField', 'JobSatisfaction', 'EnvironmentSatisfaction', 'WorkLifeBalance',
                    'StockOptionLevel', 'Gender', 'PerformanceRating', 'JobInvolvement', 'JobLevel', 'JobRole', 'MaritalStatus', 'RelationshipSatisfaction']

        to_get_dummies_for = ['BusinessTravel', 'Department', 'Education', 'EducationField', 'EnvironmentSatisfaction', 'Gender', 'JobInvolvement', 'JobLevel', 'JobRole', 'MaritalStatus']

        df = create_dummy_variables(df, to_get_dummies_for)
        df = map_binary_columns(df)
        df = engineer_features(df)

        Y = df['Attrition']
        X = df.drop(columns=['Attrition'])

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        logging.info("Data preprocessing completed successfully")
        return pd.DataFrame(X_scaled, columns=X.columns), Y, num_cols, cat_cols
    except Exception as e:
        logging.error("Error in data preprocessing: %s", e)
        raise