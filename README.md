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
