README for Bank Marketing Campaign Data Analysis

Introduction
This repository contains code and information related to the analysis of a dataset from a bank marketing campaign. The analysis includes data preprocessing, outlier removal, feature scaling, feature selection, and building a logistic regression model. The primary goal is to predict the success of a marketing campaign based on various features.

Dataset
The dataset used in this analysis is related to a marketing campaign conducted by a bank. It includes various features such as age, campaign details, economic indicators, and more. The target variable is binary, indicating whether a client subscribed to a term deposit ("yes") or not ("no").

Contents
Data Cleaning and Outlier Removal

The dataset is loaded, and outliers are removed based on predefined limits for specific variables.
Feature Scaling

The numerical features are scaled using standardization (Z-score normalization).
Feature Selection

Feature selection is performed using the chi-squared statistical test.
Logistic Regression Model

A logistic regression model is constructed using the preprocessed data.
Model accuracy is evaluated, and a confusion matrix is visualized to understand model performance.
Hyperparameter Optimization

Grid search and random search techniques are employed to optimize hyperparameters for the logistic regression model.
Model Improvement

The model is further improved based on the optimized hyperparameters.
The percentage improvement in accuracy is calculated.
Instructions
Clone the repository to your local machine.
Ensure you have the required Python libraries installed (pandas, scikit-learn, matplotlib, seaborn).
Run the Jupyter Notebook files in the provided order.
Note
The dataset used in this analysis is assumed to be already cleaned and preprocessed.
Adjustments may be needed based on the characteristics of your specific dataset.
Feel free to explore, modify, and contribute to enhance the analysis!
