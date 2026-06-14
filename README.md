# 🏦 Credit Card Fraud Detection - FinBank AI Control Room

🔗 GitHub Repository:  
https://github.com/shariqua06/credit-card-fraud-detection

---
## Internship Details

- Internship Provider: CodTech IT Solutions  
- Intern ID: CITS3942  
- Internship Week: Week 4  
- Intern Name: Shariqua Tabassum G  

---

## Project Title

AI-Powered Credit Card Fraud Detection System (FinTech Dashboard)

---

## Project Overview

This project is a FinTech-style AI fraud detection control room built using Python and Streamlit.  
It simulates real-world banking transaction monitoring where an AI model detects fraudulent transactions using machine learning trained on a credit card dataset.  
The system provides a live dashboard experience similar to banking fraud monitoring systems used in financial institutions.

---

## Key Features

- Safe transaction stream simulation  
- Fraud detection stream simulation  
- Real-time analytics dashboard  
- Fraud vs Safe visualization (Pie Chart)  
- Risk trend analysis (Line Chart)  
- Dark FinTech UI inspired by Stripe  
- Login authentication (admin system)  
- Fully automated simulation without manual input  
- Machine learning-powered fraud prediction  

---

## Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- Pandas  
- NumPy  
- Plotly  
- Joblib  

---

## 📂 Project Structure

credit-card-fraud-detection/
│
├── app.py
│
├── models/
│   └── fraud_model.pkl
│
├── data/
│   └── creditcard.csv
│
├── requirements.txt
│
└── README.md
---

## How to Run the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shariqua06/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   
2. **Install dependencies:**

   pip install -r requirements.txt
   
3. **Download dataset:**

   *Go to Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud (kaggle.com in Bing)
   *Download creditcard.csv
   *Place it inside a folder named data/ in the project root

4. **Train the model:**
   
   bash

    python model_training.py
   
_This will generate models/fraud_model.pkl locally.

5. **Run the Streamlit app:**
   
   bash
   streamlit run app.py
   
6.Access the dashboard in your browser (usually at http://localhost:8501)

## Login Credentials:
Username: admin
Password: admin123

## Dataset Information:
-Dataset: Credit Card Fraud Detection Dataset
-Contains anonymized real-world transactions
-Features:
   ~V1 to V28 (PCA transformed)
   ~Time
   ~Amount
   ~Class (0 = Safe, 1 = Fraud)
   
## UI/UX Design
-Dark FinTech Control Room Theme
-Glassmorphism cards with glow effect
-Animated dashboard feel
-Stripe-inspired analytics layout
-Fully responsive Streamlit UI

## Dashboard Modules
-Overview
   Total transactions scanned
   Fraud alerts
   Safe transactions
   Pie chart visualization
-Safe Stream
   Simulates safe transactions from dataset
   Displays AI risk score
-Fraud Stream
   Simulates fraud transactions from dataset
   Displays fraud alerts in real-time style
-Analytics
   Fraud vs Safe distribution
   Risk trend analysis
   Interactive charts

## Key Highlights
✔ Real-world dataset simulation
✔ Fully automated ML fraud detection
✔ FinTech-grade UI design
✔ No manual feature input required
✔ Resume-ready AI project

## Future Enhancements
   Real-time transaction API integration
   Email/SMS fraud alert system
   SHAP explainability for predictions
   Cloud deployment (Streamlit Cloud / AWS)
   Admin analytics panel upgrade

## Developed By
   Shariqua Tabassum G
   Intern - CodTech IT Solutions
   Intern ID: CITS3942
   Week 4 Internship Project

## Repository

   https://github.com/shariqua06/credit-card-fraud-detection⁠

