import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.data.data_processing import load_data, preprocess_data
from src.model.model_training import split_data, train_logistic_regression, train_svm
from src.visualization.visualization import plot_histograms, plot_category_percentages, plot_correlation_heatmap
from src.model.model_evaluation import evaluate_model
import logging

# Ensure the log file exists
log_file_exists = os.path.exists('app.log')
if not log_file_exists:
    with open('app.log', 'w') as f:
        f.write('Log file created.\n')

# Configure logging
def setup_logging():
    
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

setup_logging()

#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Load and preprocess data
        df = load_data('HR_Employee_Attrition.csv')
        X, Y, num_cols, cat_cols = preprocess_data(df)

        # Visualizations
        plot_histograms(df, num_cols)
        plot_category_percentages(df, cat_cols)
        plot_correlation_heatmap(df, num_cols)

        # Split data
        x_train, x_test, y_train, y_test = split_data(X, Y)

        # Train and evaluate Logistic Regression model
        lg_model = train_logistic_regression(x_train, y_train)
        evaluate_model(lg_model, x_test, y_test)

        # Train and evaluate SVM model with different kernels
        svm_linear = train_svm(x_train, y_train, kernel='linear')
        evaluate_model(svm_linear, x_test, y_test)

        svm_rbf = train_svm(x_train, y_train, kernel='rbf')
        evaluate_model(svm_rbf, x_test, y_test)

        svm_poly = train_svm(x_train, y_train, kernel='poly')
        evaluate_model(svm_poly, x_test, y_test)

        logging.info("Main script executed successfully")
    except Exception as e:
        logging.error("Error in main script: %s", e)
        raise

if __name__ == '__main__':
    main()