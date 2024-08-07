Employee_Attrition_Using_SVM/

Purpose
This project aims to predict employee attrition using machine learning techniques. The dataset includes various features related to employees such as age, income, job satisfaction, and more. The project involves data loading, preprocessing, model training, evaluation, and visualization.

----------

How to Run This Code

 - Ensure you have Python installed on your system along with the required packages.
 - Place HR_Employee_Attrition.csv in the directory where the script is located.
 - Run the main.py script in a Python environment.

------------

Dependencies

The following libraries are required:

pandas: For data manipulation and analysis
numpy: For numerical operations
matplotlib: For plotting graphs
seaborn: For data visualization
scikit-learn: For machine learning algorithms and evaluation metrics
logging: For logging errors and information

Ensure they are installed using pip:

pip install pandas numpy matplotlib seaborn scikit-learn

----------

Project Structure
│
├── data/
│ └── HR_Employee_Attrition.csv # The dataset file
│
├── src/
│ ├── init.py # Makes src a package
│ ├── data/
│ │ ├── init.py # Makes data a package
│ │ └── data_processing.py # Module for loading and preprocessing data
│ ├── feature/
│ │ ├── init.py # Makes feature a package
│ │ └── build_features.py # Module for feature engineering
│ ├── models/
│ │ ├── init.py # Makes models a package
│ │ ├── model_evaluation.py # Module for training models
│ │ └── model_training.py # Module for evaluating models
│ ├── visualization/
│ │ ├── init.py # Makes visualization a package
│ │ └── visualization.py # Module for data visualization
├── main.py # Main script to run the project
├── README.md # Project description and instructions
├── requirements.txt # List of dependencies
└── .gitignore # Git ignore file

------------------

Detailed Steps
1. Data Loading
The dataset is loaded from a CSV file named HR_Employee_Attrition.csv using the load_data function from data_processing.py. This function reads the data into a pandas DataFrame and performs initial preprocessing.
2. Data Preprocessing
Preprocess Data: The preprocess_data function in data_processing.py handles the data preprocessing steps including scaling numerical features and encoding categorical features.
Drop Unnecessary Columns: Remove columns that are not needed for the analysis, such as EmployeeNumber, Over18, and StandardHours.
Create Dummy Variables: Convert categorical variables into dummy variables to prepare the data for machine learning algorithms.
Map Binary Columns: Map binary columns to numerical values.
Feature Engineering: Create new features such as TotalExperienceRatio and SalaryToExperienceRatio.
3. Data Splitting
Split Data: The split_data function in model_training.py splits the data into training and testing sets.
4. Model Training
Logistic Regression: Train a logistic regression model using the train_logistic_regression function.
Support Vector Machine (SVM): Train an SVM model with different kernels (linear, rbf, poly) using the train_svm function.
5. Model Evaluation
Evaluate Models: The evaluate_model function in model_evaluation.py evaluates the models on the test data and prints the metrics score.
Confusion Matrix: Plot the confusion matrix for the predictions.
6. Visualization
Plot Histograms: The plot_histograms function in visualization.py plots histograms for numerical features.
Plot Category Percentages: The plot_category_percentages function plots the percentage distribution of categorical features.
Plot Correlation Heatmap: The plot_correlation_heatmap function plots the correlation heatmap for numerical features.

----------

Conclusion
This project demonstrates a complete workflow for predicting employee attrition using machine learning. It covers data preprocessing, model training, evaluation, and visualization. The models are evaluated using accuracy scores and confusion matrices to ensure robustness and reliability. The logistic regression and SVM models provide a comprehensive approach to understanding and predicting employee attrition based on various features.


---------------

Steps to Push code from VS code to Github.
First authenticate your githib account and integrate with VS code. Click on the source control icon and complete the setup.
1. Click terminal and open new terminal
2. git config --global user.name "Swapnilin"
3. git config --global user.email swapnilforcat@gmail.com
4. git init
5. git add .
6. git commit -m "Your commit message"