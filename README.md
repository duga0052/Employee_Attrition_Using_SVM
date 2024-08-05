Classification - Loan Approval Model
==============================

Employee_Attrition_Using_SVM/
│
├── src/
│ ├── init.py
│ ├── data/
│ │ ├── init.py
│ │ ├── data_processing.py
│ ├── feature/
│ │ ├── init.py
│ │ ├── build_features.py
│ ├── models/
│ │ ├── init.py
│ │ ├── train_model.py
│ │ ├── evaluate_model.py
│ ├── visualization/
│ │ ├── init.py
│ │ ├── visualization.py
│
├── main.py
├── requirements.txt
└── README.md



### File Descriptions
- `src/data/data_processing.py`: Contains functions for loading and preprocessing data.
- `src/feature/build_features.py`: Includes functions for creating new features and transforming existing ones.
- `src/models/train_model.py`: Contains functions for training machine learning models.
- `src/models/evaluate_model.py`: Contains functions for evaluating machine learning models.
- `src/visualization/visualization.py`: Provides functions for creating various plots and visualizations.
- `main.py`: The main script that orchestrates the entire process.
- `requirements.txt`: Lists the dependencies required to run the project.
- `README.md`: This file, providing an overview of the project.

## Logging and Error Handling
The project includes logging and error handling mechanisms to ensure robust execution. Logs provide information about the progress and any issues encountered during execution.

--------

Steps to Push code from VS code to Github.
First authenticate your githib account and integrate with VS code. Click on the source control icon and complete the setup.
1. Click terminal and open new terminal
2. git config --global user.name "Swapnilin"
3. git config --global user.email swapnilforcat@gmail.com
4. git init
5. git add .
6. git commit -m "Your commit message"