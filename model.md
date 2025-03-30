# Model Architecture

## Overview
This project implements multiple machine learning models to detect money laundering activities based on financial transaction data. The models used include:

- **Decision Tree Classifier**
- **XGBoost (Extreme Gradient Boosting)**
- **LightGBM (Light Gradient Boosting Machine)**
- **CatBoost (Categorical Boosting)**

Each model is trained and evaluated to determine the most effective approach for Anti-Money Laundering (AML) detection.

---

## Model Details

### 1. Decision Tree Classifier
- A simple yet effective classification model that splits the data into branches based on feature importance.
- Works well with interpretable rules but can overfit without proper pruning.
- Implemented using `sklearn.tree.DecisionTreeClassifier`.

### 2. XGBoost
- A powerful gradient boosting algorithm optimized for speed and performance.
- Utilizes boosting to sequentially improve weak learners.
- Implemented using `xgboost.XGBClassifier`.

### 3. LightGBM
- A highly efficient and scalable gradient boosting framework.
- Faster training speed and lower memory usage than XGBoost.
- Implemented using `lightgbm.LGBMClassifier`.

### 4. CatBoost
- A high-performance gradient boosting model optimized for categorical data.
- Uses Ordered Boosting to prevent overfitting.
- Implemented using `catboost.CatBoostClassifier`.

---

## Model Training & Evaluation

1. **Data Preprocessing:**
   - Encoding categorical features.
   - Handling missing values and feature selection.
   - Normalizing numerical data.

2. **Model Training:**
   - Training each model with labeled transaction data.
   - Using `train_test_split()` to divide data into training and testing sets.

3. **Evaluation Metrics:**
   - Accuracy
   - Precision, Recall, F1-score
   - ROC-AUC Curve

Each model is compared based on these evaluation metrics to determine the most suitable approach for AML detection.

---

## Deployment
- The trained models are stored in the `/model/` directory for further analysis or real-time deployment.
- Predictions can be made using the trained models to detect fraudulent transactions.

---

## Future Improvements
- Implementing deep learning models like LSTMs for sequential transaction analysis.
- Exploring graph-based methods to detect complex laundering patterns.

