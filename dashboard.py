import streamlit as st
import pickle
import numpy as np

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="Trader AI Dashboard", layout="wide")

st.title("📊 AI Trade Profit Predictor")
st.write("Predict if trade will be profitable based on sentiment & trade size")

# ==============================
# LOAD MODEL
# ==============================
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()
st.success("✅ Model loaded successfully")

# ==============================
# USER INPUTS
# ==============================
st.sidebar.header("Enter Trade Details")

trade_size = st.sidebar.number_input("Trade Size (USD)", value=100.0)

sentiment_option = st.sidebar.selectbox(
    "Market Sentiment",
    ["Extreme Fear","Fear","Neutral","Greed","Extreme Greed"]
)

# same encoding used in training
sentiment_map = {
    "Extreme Fear":0,
    "Fear":1,
    "Neutral":2,
    "Greed":3,
    "Extreme Greed":4
}

sentiment_value = sentiment_map[sentiment_option]

# ==============================
# PREDICTION
# ==============================
st.subheader("Prediction Result")

if st.sidebar.button("Predict Now"):

    # must match training features order
    input_data = np.array([[trade_size, sentiment_value]])

    prediction = model.predict(input_data)[0]

    if prediction:
        st.success("🟢 Trade likely PROFITABLE")
    else:
        st.error("🔴 Trade likely LOSS")

# ==============================
# INFO SECTION
# ==============================
st.markdown("---")
st.subheader("About Model")

st.write("""
This model predicts trade profitability using:
- Trade size
- Market sentiment (Fear/Greed)

Built for Primetrade.ai Data Science Intern assignment.
""")

st.subheader("Strategy Insights")

st.write("""
✔ Larger trades during Greed have higher success probability  
✔ Fear markets show higher loss probability  
✔ Use controlled position sizing in volatile markets  
""")

st.success("🚀 Dashboard Ready for Submission")
