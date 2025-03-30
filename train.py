import pandas as pd
import xgboost as xgb
import lightgbm as lgb
import catboost as cb
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load processed data
X_train = pd.read_csv("dataset/X_train.csv")
X_test = pd.read_csv("dataset/X_test.csv")
y_train = pd.read_csv("dataset/y_train.csv").values.ravel()
y_test = pd.read_csv("dataset/y_test.csv").values.ravel()

# Initialize models
models = {
    "Decision Tree": DecisionTreeClassifier(),
    "XGBoost": xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss"),
    "LightGBM": lgb.LGBMClassifier(),
    "CatBoost": cb.CatBoostClassifier(verbose=0)
}

# Train and evaluate models
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model: {name}, Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))
