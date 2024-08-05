import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_dummy_variables(df, columns_to_dummify):
    try:
        df = pd.get_dummies(data=df, columns=columns_to_dummify, drop_first=True)
        logging.info("Dummy variables created for columns: %s", columns_to_dummify)
        return df
    except Exception as e:
        logging.error("Error creating dummy variables: %s", e)
        raise

def map_binary_columns(df):
    try:
        df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
        df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
        logging.info("Binary columns mapped successfully")
        return df
    except Exception as e:
        logging.error("Error mapping binary columns: %s", e)
        raise

def engineer_features(df):
    try:
        df['TotalExperienceRatio'] = df['TotalWorkingYears'] / df['Age']
        df['SalaryToExperienceRatio'] = df['MonthlyIncome'] / (df['TotalWorkingYears'] + 1)  # Adding 1 to avoid division by zero
        logging.info("Feature engineering completed successfully")
        return df
    except Exception as e:
        logging.error("Error in feature engineering: %s", e)
        raise