import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_histograms(df, num_cols):
    try:
        df[num_cols].hist(figsize=(14,14))
        plt.tight_layout()
        plt.show()
        logging.info("Histograms plotted successfully")
    except Exception as e:
        logging.error("Error plotting histograms: %s", e)
        raise

def plot_category_percentages(df, cat_cols):
    try:
        for col in cat_cols:
            print(df[col].value_counts(normalize=True))
            print('*'*40)
            
            if col != 'Attrition':
                (pd.crosstab(df[col], df['Attrition'], normalize='index')*100).plot(kind='bar', figsize=(8,4), stacked=True)
                plt.ylabel('Percentage Attrition %')
                plt.title(f'Attrition by {col}')
                plt.tight_layout()
                plt.show()
        logging.info("Category percentages plotted successfully")
    except Exception as e:
        logging.error("Error plotting category percentages: %s", e)
        raise

def plot_correlation_heatmap(df, num_cols):
    try:
        plt.figure(figsize=(15,8))
        sns.heatmap(df[num_cols].corr(), annot=True, fmt='0.2f', cmap='YlGnBu')
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.show()
        logging.info("Correlation heatmap plotted successfully")
    except Exception as e:
        logging.error("Error plotting correlation heatmap: %s", e)
        raise