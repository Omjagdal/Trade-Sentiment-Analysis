# 📊 Trader Performance vs Market Sentiment Analysis

### Primetrade.ai — Data Science Intern Assignment

## 🧠 Objective

The goal of this project is to analyze how market sentiment (Fear/Greed) impacts trader behavior and profitability on Hyperliquid.
This analysis identifies patterns in trading activity, risk-taking, and performance across different market sentiment conditions and provides actionable strategy insights.

---

## 📁 Datasets Used

### 1. Bitcoin Market Sentiment Dataset

* Daily sentiment classification: Fear, Greed, Extreme Fear, etc.
* Used to understand overall market psychology.

### 2. Historical Trader Dataset (Hyperliquid)

Includes detailed trade-level information:

* Account
* Symbol
* Trade size (USD)
* Side (Long/Short)
* Closed PnL
* Timestamp
* Market sentiment (merged)

---

## ⚙️ Project Workflow

### 1. Data Cleaning & Preparation

* Loaded and inspected datasets
* Handled missing values and duplicates
* Converted timestamps to datetime
* Merged trader data with sentiment data on daily level

### 2. Feature Engineering

Created key metrics:

* Daily PnL per trader
* Win rate (profit vs loss trades)
* Average trade size
* Trade frequency
* Long vs short behavior
* Sentiment-based performance

### 3. Exploratory Data Analysis

Analyzed how trader behavior changes with sentiment:

* Profitability across Fear vs Greed markets
* Trading frequency changes
* Risk exposure through trade size
* Behavioral patterns across market conditions

### 4. Trader Segmentation

Traders grouped into behavioral segments:

* High-frequency vs low-frequency traders
* Consistent profitable vs inconsistent traders
* Risk-taking behavior patterns

This helped identify performance differences between trader types.

---

## 🤖 Machine Learning Model

A simple classification model was built to predict whether a trade will be profitable using:

* Trade size (USD)
* Market sentiment (encoded)

The model was saved as a pickle file and deployed into a Streamlit dashboard for real-time prediction.

---

## 📊 Streamlit Dashboard

An interactive dashboard was created to:

* Input trade size and sentiment
* Predict trade profitability
* Provide risk insights and strategy suggestions

This demonstrates practical deployment of data science insights.

Run locally:

```bash
streamlit run dashboard.py
```

---

## 🔑 Key Insights

* Trader profitability varies significantly across market sentiment.
* Fear markets show higher volatility and increased losses.
* Greed sentiment encourages larger trade sizes and higher activity.
* Trade size strongly influences profit/loss outcomes.

---

## 💡 Strategy Recommendations

* Reduce position size during Fear markets to control risk.
* Increase trade activity cautiously during Greed sentiment.
* Avoid overexposure in highly volatile periods.
* Apply risk management based on sentiment conditions.

---

## 🛠 Tech Stack

* Python
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn
* Streamlit

---

## ▶️ How to Run Project

1. Clone repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run Jupyter notebook for analysis
4. Launch dashboard

```bash
streamlit run dashboard.py
```

---

## 👤 Author

Om Jagdale
Aspiring Data Scientist
Primetrade.ai Internship Applicant
