import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import time

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="FinBank AI Control Room",
    page_icon="🏦",
    layout="wide"
)

# ---------------- LOAD ----------------
model = joblib.load("models/fraud_model.pkl")
df = pd.read_csv("data/creditcard.csv")

# ---------------- SESSION ----------------
if "login" not in st.session_state:
    st.session_state.login = False
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- ULTRA FINTECH UI ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #050F24, #020814);
    color: white !important;
}
* {
    color: white !important;
    font-family: Arial;
}
[data-testid="stSidebar"] {
    background-color: #071428 !important;
}
.stButton>button {
    background: linear-gradient(90deg, #1E90FF, #00C2FF);
    border-radius: 10px;
    font-weight: bold;
    color: white !important;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px #00C2FF;
}
.card {
    background: rgba(255,255,255,0.06);
    border: 1px solid #1E90FF;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 0 15px rgba(0,194,255,0.15);
    transition: 0.3s;
}
.card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 25px rgba(0,194,255,0.35);
}
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid #1E90FF;
    border-radius: 12px;
}
h1, h2, h3 {
    color: #4DA3FF !important;
}
.stDataFrame {
    background-color: #050F24 !important;
    color: white !important;
}

/* LOGIN INPUT TEXT ONLY */
input[type="text"], input[type="password"] {
    color: black !important;        /* typed text is black */
    background-color: #f0f0f0 !important;  /* light background for contrast */
    border-radius: 6px;
    padding: 6px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
def login():
    st.title("🏦 FinBank AI Control Room")
    st.info("Demo Login → admin / admin123")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        if u == "admin" and p == "admin123":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid credentials")

# ---------------- DASHBOARD ----------------
def dashboard():
    menu = st.sidebar.radio(
        "CONTROL PANEL",
        ["🏠 Overview", "🟢 Safe Stream", "🔴 Fraud Stream", "📊 Analytics", "🚪 Logout"]
    )

    # Overview
    if menu == "🏠 Overview":
        st.title("🏦 LIVE FINTECH CONTROL DASHBOARD")
        total = len(st.session_state.history)
        fraud = sum(1 for x in st.session_state.history if x["result"] == "FRAUD")
        safe = total - fraud

        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(f"<div class='card'><h3>Transactions</h3><h2>{total}</h2></div>", unsafe_allow_html=True)
        with col2: st.markdown(f"<div class='card'><h3>Fraud Alerts</h3><h2>{fraud}</h2></div>", unsafe_allow_html=True)
        with col3: st.markdown(f"<div class='card'><h3>Safe Transactions</h3><h2>{safe}</h2></div>", unsafe_allow_html=True)

        st.markdown("### 🔵 System Status: LIVE AI MONITORING ACTIVE")

        if total > 0:
            dfh = pd.DataFrame(st.session_state.history)
            fig = px.pie(dfh, names="result", hole=0.5, title="Transaction Flow",
                         color="result", color_discrete_map={"SAFE":"#00FF99","FRAUD":"#FF3366"})
            fig.update_traces(marker=dict(line=dict(color="white", width=2)))
            fig.update_layout(paper_bgcolor="#050F24", plot_bgcolor="#050F24",
                              font_color="white", title_font_color="#00C2FF")
            st.plotly_chart(fig, use_container_width=True)

    # Safe Stream
    elif menu == "🟢 Safe Stream":
        st.title("🟢 Safe Transaction Feed (Dataset Driven)")
        samples = df[df["Class"] == 0].sample(5)
        for _, row in samples.iterrows():
            x = row.drop("Class").values
            prob = model.predict_proba([x])[0][1]
            st.markdown(f"""
            <div class="card">
                <h3>🟢 SAFE TRANSACTION</h3>
                <p>Risk Score: {prob:.5f}</p>
                <p>Status: APPROVED</p>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append({"result":"SAFE","risk":prob})
            time.sleep(0.2)
        st.success("Safe stream completed")

    # Fraud Stream
    elif menu == "🔴 Fraud Stream":
        st.title("🔴 Fraud Alert Feed (Dataset Driven)")
        samples = df[df["Class"] == 1].sample(5)
        for _, row in samples.iterrows():
            x = row.drop("Class").values
            prob = model.predict_proba([x])[0][1]
            st.markdown(f"""
            <div class="card">
                <h3>🚨 FRAUD DETECTED</h3>
                <p>Risk Score: {prob:.5f}</p>
                <p>Status: BLOCKED</p>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append({"result":"FRAUD","risk":prob})
            time.sleep(0.2)
        st.error("Fraud stream completed")

    # Analytics
    elif menu == "📊 Analytics":
        st.title("📊 FINTECH ANALYTICS DASHBOARD")
        if len(st.session_state.history) == 0:
            st.warning("No data yet. Run streams first.")
            return
        dfh = pd.DataFrame(st.session_state.history)
        col1, col2, col3 = st.columns(3)
        with col1:
            fig = px.pie(dfh, names="result", hole=0.4, title="Fraud vs Safe Distribution",
                         color="result", color_discrete_map={"SAFE":"#00FF99","FRAUD":"#FF3366"})
            fig.update_traces(marker=dict(line=dict(color="white", width=2)))
            fig.update_layout(paper_bgcolor="#050F24", plot_bgcolor="#050F24",
                              font_color="white", title_font_color="#00C2FF")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig2 = px.line(dfh, y="risk", title="Risk Trend Over Time",
                           markers=True, line_shape="spline",
                           color_discrete_sequence=["#4DA3FF"])
            fig2.update_traces(line=dict(width=3), marker=dict(size=8, line=dict(width=2, color="white")))
            fig2.update_layout(paper_bgcolor="#050F24", plot_bgcolor="#050F24",
                               font_color="white", title_font_color="#00C2FF")
            st.plotly_chart(fig2, use_container_width=True)
        with col3:
            dfh["index"] = range(len(dfh))
            fig3 = px.bar(dfh, x="index", color="result", title="Fraud vs Safe Counts Over Time",
                          color_discrete_map={"SAFE":"#00FF99","FRAUD":"#FF3366"})
            fig3.update_layout(paper_bgcolor="#050F24", plot_bgcolor="#050F24",
                               font_color="white", title_font_color="#00C2FF")
            st.plotly_chart(fig3, use_container_width=True)
        st.dataframe(dfh)

    # Logout
    elif menu == "🚪 Logout":
        st.session_state.login = False
        st.rerun()

# ---------------- RUN ----------------
if st.session_state.login:
    dashboard()
else:
    login()
