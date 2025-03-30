# 📌 Anti-Money Laundering Dataset

## 📊 Overview
This dataset contains financial transaction records used for detecting money laundering activities using machine learning models. 
Each transaction is labeled as either **money laundering (`1`)** or **legitimate (`0`)** to help train fraud detection systems.

The dataset includes various attributes such as **bank details, account numbers, transaction amounts, currencies, and payment formats** 
to simulate real-world financial transactions.

---

## 📁 Dataset Structure
```
dataset/
│── train/                      # Training data (80%)
│── test/                       # Test data (10%)
│── val/                        # Validation data (10%)
│── HI-Small_Trans.csv          # High illicit ratio (small dataset)
│── HI-Medium_Trans.csv         # High illicit ratio (medium dataset)
│── HI-Large_Trans.csv          # High illicit ratio (large dataset)
│── LI-Small_Trans.csv          # Low illicit ratio (small dataset)
│── LI-Medium_Trans.csv         # Low illicit ratio (medium dataset)
│── LI-Large_Trans.csv          # Low illicit ratio (large dataset)
```

---

## 📝 Feature Descriptions

| **Feature Name**       | **Description** |
|------------------------|----------------|
| `Timestamp`           | Date and time of the transaction |
| `From_Bank`          | Identifier of the sending bank |
| `From_Account`       | Unique ID of the sender’s account |
| `To_Bank`            | Identifier of the receiving bank |
| `To_Account`         | Unique ID of the recipient’s account |
| `Amount_Received`    | Amount credited to the recipient |
| `Receiving_Currency` | Currency type of received amount |
| `Amount_Paid`       | Amount debited from the sender |
| `Payment_Currency`   | Currency type of the payment |
| `Payment_Format`     | Type of transaction (Wire Transfer, Crypto, Cash, etc.) |
| `Is_Laundering`      | **Target Variable** (1 = Money Laundering, 0 = Legitimate) |

---

## 🔍 Class Distribution
- **`1` (Money Laundering)** → Suspicious financial transactions  
- **`0` (Legitimate Transactions)** → Normal financial transactions  

---

## 📌 Source
This dataset is based on IBM’s **Synthetic Financial Transactions for Anti-Money Laundering (AML)**. 
It is designed to simulate real-world financial activity patterns involving potential fraud cases.

---

## 💡 Usage
This dataset is suitable for:  
✅ **Machine Learning-based Fraud Detection**  
✅ **Graph-Based Financial Transaction Analysis**  
✅ **Anomaly Detection in Banking Systems**  

### 📌 Models that can be trained:  
- Decision Tree  
- XGBoost (XGB)  
- LightGBM (LGB)  
- CatBoost  

---

## 📌 Preprocessing Notes
- Encode categorical variables such as `From_Bank`, `To_Bank`, `Payment_Format`, etc.  
- Handle missing values if any.  
- Normalize numerical features (`Amount_Received`, `Amount_Paid`).  
- Split data into **train (80%), validation (10%), and test (10%)**.  

---

## 📜 Citation
If you use this dataset, please credit IBM’s **Synthetic Financial Transactions for AML** dataset.
