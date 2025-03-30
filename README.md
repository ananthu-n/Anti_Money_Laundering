# 💰 Anti-Money Laundering (AML) Detection using Machine Learning

##  Project Overview
Money laundering is a significant global financial crime that involves disguising the origins of illegally obtained money. This project aims to **detect money laundering transactions** using machine learning models.

We use a **synthetic financial transactions dataset** from IBM, which contains labeled data distinguishing between **legitimate** and **laundering** transactions. The goal is to train models that can accurately detect suspicious transactions while minimizing false positives.

## 📂 Dataset Information
The dataset includes financial transactions with details such as:
✅ **Transaction timestamps**  
✅ **Bank and account details**  
✅ **Amounts received and paid**  
✅ **Currency types and payment format**  
✅ **Labeled laundering transactions (1 = laundering, 0 = legitimate)**  

The dataset is divided into **six variations** based on transaction volume and laundering ratio (High Illicit (HI) and Low Illicit (LI)).

## 📊 Machine Learning Models Used
We implement and compare the following models for classification:
✅ **Decision Tree** – A simple and interpretable model.  
✅ **XGBoost** – A powerful gradient boosting model optimized for structured data.  
✅ **LightGBM** – A fast and efficient tree-based model for large-scale data.  
✅ **CatBoost** – A high-performance model designed for categorical features.  

---

## 🧠 Model Architecture
The architecture consists of the following steps:

1️⃣ **Data Preprocessing:**  
   - Convert **timestamps** into numerical features (hour, day, month).  
   - Encode **categorical features** (banks, currency types, payment formats).  
   - Drop **non-informative columns** (account numbers).  
   - Split the dataset into **training (80%)** and **testing (20%)** sets.  

2️⃣ **Feature Selection & Engineering:**  
   - Identify the most **informative features** using correlation analysis.  
   - Scale numerical features if necessary.  

3️⃣ **Model Training:**  
   - Train **Decision Tree, XGBoost, LightGBM, and CatBoost** models.  
   - Use **hyperparameter tuning** to optimize performance.  

4️⃣ **Model Evaluation:**  
   - Compare models using **Accuracy, Precision, Recall, F1-score, and ROC-AUC**.  
   - Identify the best-performing model.  

5️⃣ **Model Deployment (Future Work):**  
   - Save the trained model using **joblib** or **pickle**.  
   - Deploy as a **REST API or web application** for real-time detection.  

---

## 📌 Project Structure
```
Anti-Money-Laundering-Detection/
│── Anti_Money_Laundering.ipynb  # Jupyter notebook for training & evaluation
│── README.md                    # Project documentation
│── requirements.txt             # Dependencies
│── preprocessing.py             # Data preprocessing script
│── train.py                     # Model training script
│── model/                       # Saved trained models (Decision Tree, XGBoost, LightGBM, CatBoost)
│── dataset/                      # Kaggle dataset files
           # Kaggle dataset files
```

---

## 📊 Model Evaluation
We evaluate the models using:  
✅ **Accuracy** – Measures overall correctness.  
✅ **Precision & Recall** – Balances false positives & false negatives.  
✅ **F1-Score** – Harmonic mean of precision and recall.  
✅ **ROC-AUC** – Measures the model's ability to distinguish laundering from legitimate transactions.  

---

## 🚀 How to Run the Project
### 1️⃣ Clone the repository  
```bash
git clone https://github.com/yourusername/Anti-Money-Laundering-Detection.git
cd Anti-Money-Laundering-Detection
```
### 2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```
### 3️⃣ Run preprocessing & training  
```bash
python src/preprocess.py  
python src/train.py  
```
### 4️⃣ Evaluate the model  
```bash
python src/evaluate.py  
```

---

## 💡 Future Improvements
🔹 Implement **Deep Learning models** for better fraud detection.  
🔹 Use **Graph Neural Networks (GNNs)** for detecting transaction patterns.  
🔹 Deploy an **API-based AML detection system**.  

---


