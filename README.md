# 🏠 Bangalore House Price Prediction Web App

A Machine Learning-powered web application that predicts house prices in Bangalore based on user inputs like location, square footage, number of bathrooms, and BHK (bedrooms, halls, kitchens). Built with **Streamlit**, trained using **Linear Regression**, and deployed on the **Streamlit Cloud**.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live-green)](https://housepriceprediction-3gx6wpblt9adukai3mbvhs.streamlit.app/)

---

## 📌 Project Overview

This project helps users estimate real estate prices in Bangalore using a machine learning model trained on real housing data. It demonstrates the complete ML pipeline — from preprocessing and model training to web deployment.

---

## 🧠 Model and Approach

### ✅ Problem Type: 
- Supervised Learning (Regression)

### ✅ Model Used: 
- **Linear Regression** (Best Performance)

### ✅ Evaluation Metric: 
- **R² Score (Coefficient of Determination)**

### ✅ Models Compared:

| Model              | Best R² Score | Best Parameters |
|-------------------|---------------|------------------|
| **Linear Regression** | **0.8487**    | No tuning needed |
| Lasso Regression  | 0.8446        | `{'alpha': 0.01, 'max_iter': 1000}` |
| Decision Tree     | 0.7661        | `{'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10}` |

✅ Used **5-Fold Cross Validation** and **GridSearchCV** for hyperparameter tuning.

---

## 🛠️ Tech Stack

| Tool/Library        | Purpose                          |
|---------------------|----------------------------------|
| **Python**          | Programming Language             |
| **pandas, numpy**   | Data manipulation and analysis   |
| **matplotlib, seaborn** | Visualization tools       |
| **scikit-learn**    | Model training & evaluation      |
| **Streamlit**       | Web app development              |
| **GitHub**          | Code hosting                     |
| **Streamlit Cloud** | Deployment                       |

---

## 📂 Project Structure

House_Price_Prediction/

  ├── app.py # Streamlit web app

  ├── model.pickle # Trained Linear Regression model

  ├── columns.json # One-hot encoded feature columns

  ├── Image.png # Background image

  ├── requirements.txt # Python dependencies

  ├── Corrected_House_Price_Prediction.ipynb # Full ML pipeline

  └── README.md # Project documentation


---

## 🔄 ML Pipeline – Step by Step

### 1️⃣ Data Cleaning & Preprocessing
- Removed outliers (e.g., unrealistic sqft per BHK)
- One-hot encoded categorical columns (`location`, `area_type`)
- Dropped invalid and missing entries

### 2️⃣ Feature Engineering
- Selected key features: `total_sqft`, `bath`, `bhk`, `location`, `area_type`
- Final columns stored in `columns.json`

### 3️⃣ Model Training
- Trained a **Linear Regression** model (best R² score: **0.8487**)
- Saved the model as `model.pickle`

### 4️⃣ Web Application
- Built using **Streamlit**
- Clean UI with background image
- Users input details and get predicted house price in 💰 green and bold

### 5️⃣ Deployment
- Hosted on **Streamlit Cloud**
- Runs directly using `streamlit run app.py`

---

## 📷 Screenshots

### 📈 Prediction Display

![Screenshot 2025-06-13 102224](https://github.com/user-attachments/assets/d5ae84f3-3692-402f-8950-89df928d30b6)


---

## 🚀 How to Run the App Locally

```bash
# Clone the repository
git clone https://github.com/Ankita-Kumari0309/House_price_prediction.git
cd House_price_prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


