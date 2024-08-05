from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def metrics_score(actual, predicted):
    """
    Prints the classification report and plots the confusion matrix.
    """
    try:
        logging.info("Generating classification report")
        print(classification_report(actual, predicted))
        
        cm = confusion_matrix(actual, predicted)
        plt.figure(figsize=(8, 5))
        sns.heatmap(cm, annot=True, fmt='.2f', xticklabels=['Not Attrite', 'Attrite'], yticklabels=['Not Attrite', 'Attrite'])
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.title('Confusion Matrix')
        plt.tight_layout()
        plt.show()
        logging.info("Confusion matrix plotted successfully")
    except Exception as e:
        logging.error("Error in generating metrics score: %s", e)
        raise

def evaluate_model(model, x_test, y_test):
    """
    Evaluates the model on the test data and prints the metrics score.
    """
    try:
        logging.info("Evaluating model")
        y_pred = model.predict(x_test)
        metrics_score(y_test, y_pred)
    except Exception as e:
        logging.error("Error evaluating model: %s", e)
        raise