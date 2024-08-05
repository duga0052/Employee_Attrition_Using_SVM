from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def split_data(X, Y):
    try:
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1, stratify=Y)
        logging.info("Data split into training and testing sets")
        return x_train, x_test, y_train, y_test
    except Exception as e:
        logging.error("Error splitting data: %s", e)
        raise

def train_logistic_regression(x_train, y_train):
    try:
        lg = LogisticRegression()
        lg.fit(x_train, y_train)
        logging.info("Logistic Regression model trained successfully")
        return lg
    except Exception as e:
        logging.error("Error training Logistic Regression model: %s", e)
        raise

def train_svm(x_train, y_train, kernel='linear'):
    try:
        svm = SVC(kernel=kernel)
        model = svm.fit(x_train, y_train)
        logging.info("SVM model with %s kernel trained successfully", kernel)
        return model
    except Exception as e:
        logging.error("Error training SVM model: %s", e)
        raise