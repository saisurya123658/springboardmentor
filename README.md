# 🏏 IPL Win Predictor

A Streamlit-based web application that predicts the probability of a team winning an IPL match based on the current match situation.

This project uses a trained machine learning model to estimate win/loss probabilities using features like runs left, balls left, wickets, current run rate, and required run rate.

---

## 🚀 Features

- Select batting team, bowling team, and match city  
- Enter live match details (target, score, overs, wickets)  
- Predict real-time winning probability  
- Modern, styled UI with progress bars and metrics  
- Built using Streamlit and Scikit-learn  

---

## 🧠 Machine Learning Model

The model is loaded from a pre-trained pipeline stored in:



**pipe.pkl**


It uses features such as:
- Batting team  
- Bowling team  
- City  
- Runs left  
- Balls left  
- Wickets left  
- Current run rate  
- Required run rate  

The model outputs win and loss probabilities using `predict_proba`.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- Pickle  

---

## 📂 Project Structure



.
├── app.py # Main Streamlit application
├── pipe.pkl # Trained ML pipeline
├── requirements.txt # Project dependencies
├── Procfile # For deployment (Heroku, etc.)
├── setup.sh # Setup script
├── README.md # Project documentation


---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/singhshrasti/IPL-Win-Probability-Predictor.git
cd IPL-Win-Probability-Predictor

### 2. Create and activate virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows

### 3. Install dependencies
pip install -r requirements.txt
**
### 4. Run the Streamlit app
streamlit run app.py
Open in browser:
http://localhost:8501
