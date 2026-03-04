Student Performance Prediction (Machine Learning Project)

   Overview

This project develops a Machine Learning classification model to predict whether a student will pass or fail based on academic, demographic, and behavioral features.

The final grade (G3) was transformed into a binary target variable:

Pass (1) → Grade ≥ 10

Fail (0) → Grade < 10

The objective is to analyze factors influencing student performance and evaluate different classification models.

   Tech Stack

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

  Project Workflow

Data Loading and Inspection

Target Variable Creation

Exploratory Data Analysis (EDA)

Data Preprocessing (One-Hot Encoding)

Train-Test Split

Model Training

Logistic Regression

Random Forest Classifier

Model Evaluation

Feature Importance Analysis

  Results

The Random Forest model achieved strong predictive performance on the test dataset.

Previous academic grades (G1 and G2) were identified as the most influential predictors.

Study time and attendance-related features also contributed significantly.

These results highlight the importance of academic consistency and engagement in predicting student success.

 Project Structure
student-performance-ml/
│
├── student_performance_model.ipynb
├── requirements.txt
└── README.md

 Key Learnings

Converting a regression variable into a classification problem

Handling categorical variables using one-hot encoding

Comparing linear and tree-based models

Evaluating classification performance using accuracy and classification reports

Interpreting feature importance

 Limitations

High correlation between previous grades and final grade may introduce data leakage.

Hyperparameter tuning and cross-validation were not implemented in this version.

The dataset size is relatively small.

 Future Improvements

Remove grade-based leakage features

Perform hyperparameter optimization

Apply cross-validation

Deploy as an interactive web application using Streamlit

Extend the model for real-world academic intervention systems

👩🏽‍💻 Author

Habiba Musa
Aspiring AI & Machine Learning Engineer
