
# 📊 Tracker — AI Stock Dashboard

An advanced AI-powered stock analytics and forecasting dashboard built with **Streamlit**, featuring real-time stock cards, deep learning & statistical models, technical indicators, financial news, and a smart assistant — all in a stunning dark UI with animated charts and particle effects.

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 📈 **Stock Overview Cards** | Live price, sentiment, P/E, Beta, Market Cap, and BUY/HOLD ratings with mini trend charts. |
| 🤖 **Forecasting Tab** | Predict stock prices using LSTM (deep learning) or ARIMA (statistical model) with animated Plotly charts. |
| 💹 **Technical Indicators** | Plot Bollinger Bands, RSI, and MACD to analyze stock trends. |
| 📰 **News Feed** | Real-time stock news from NewsAPI with headline cards and read-more links. |
| 📊 **Model Evaluation** | Visual comparison of predicted vs. actual values with LSTM/ARIMA accuracy and errors. |
| 💬 **Ask AI** | Chatbot powered by OpenAI to answer questions about stocks, forecast, indicators, etc. |
| 🌌 **Modern UI Design** | Glassmorphism cards, dark mode, particle background, glowing tabs, and stylish fonts. |

---

## 📂 Project Structure

```
📁 stock_dashboard/
├── stock.py              # Main app file (Streamlit entry point)
├── overview_panel.py     # Stock cards with fundamentals + mini charts
├── forecast.py           # LSTM/ARIMA model forecast with accuracy
├── indicators.py         # Technical indicators (MA20, RSI, MACD, Bollinger)
├── news_panel.py         # Real-time stock news section
├── evaluation.py         # Predicted vs. Actual chart & model metrics
├── chatbot.py            # Ask AI chatbot using OpenAI
├── predictor.py          # LSTM & ARIMA model logic
├── styles/
│   └── style.css         # Custom dark theme + glassmorphism styling
├── models/
│   └── *.h5              # LSTM model files (AAPL, MSFT, etc.)

```

---

## 🧠 Models Used

- **LSTM (Long Short-Term Memory)** – deep learning model for time series prediction  
- **ARIMA (AutoRegressive Integrated Moving Average)** – statistical model for forecasting

---

## 🔧 Steps Performed

> A summary of the key steps taken to build the Tracker – AI Stock Dashboard.

1. **Project Setup**  
   - Created virtual environment `lstm-env` (Python 3.10.18)  
   - Installed dependencies: Streamlit, TensorFlow, yfinance, Plotly, OpenAI, etc.

2. **Forecasting Models**  
   - Implemented **LSTM** (with `.h5` models for AAPL, MSFT, etc.)  
   - Added **ARIMA** forecasting using statsmodels  
   - Visualized predictions using animated Plotly charts  

3. **Dashboard UI**  
   - Designed responsive layout with tabs: Overview, Forecast, Indicators, News, Evaluation, Ask AI  
   - Styled cards using `style.css` and added particle background  
   - Included a dark mode toggle

4. **Stock Overview & Indicators**  
   - Created overview cards with live stock data, sentiment & signal  
   - Plotted **RSI**, **Bollinger Bands**, **MACD**, and mini sparkline charts  

5. **News + AI Chatbot**  
   - Integrated latest market news via NewsAPI  
   - Added GPT-powered chatbot using OpenAI for user Q&A and AI-generated summaries  

6. **Evaluation & Export**  
   - Compared actual vs predicted charts (LSTM/ARIMA)  
   - Placeholder buttons for downloading forecast as PDF/CSV

---

## 🛠 Environment Setup

This project was built and tested with:

- 🐍 **Python**: `3.10.18`
- ⚙️ **Virtual Environment**: `lstm-env`
- 📦 Main libraries:
  - `streamlit`
  - `tensorflow`
  - `pandas`, `numpy`, `yfinance`
  - `plotly`, `matplotlib`
  - `statsmodels`, `scikit-learn`
  - `openai`
  - `requests`, `datetime`

---

## 📷 Preview

### 🌐 Overview
Displays real-time stock info in stylish glassmorphism cards.

![Overview](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/overview1.png)
![stock card](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/overview2.png)

### 📈 Forecast Tab
Switch between LSTM and ARIMA model predictions with smooth Plotly animations and AI-generated summaries.

![Forecast](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/forecast.png)

### 📉 Indicators
Visualize technical indicators like Bollinger Bands, RSI, and MACD.

![Indicators](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/indicators.png)

### 📰 News Feed
Live headlines from financial markets with time and external links.

![News section](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/news.png)

### 💬 Ask AI
Ask anything about stocks, models, or performance — get instant smart replies using OpenAI GPT.

![Chatbot](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/chatbot.png)

---

## 📊 Visualizations & Plots

### 1. 📈 Mini Line Charts in Overview
- **Where**: On each stock card
- **What**: Past 30-day closing prices
- **Why**: Snapshot of stock momentum

- ![Overview](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/overview1.png)

### 2. 🔮 LSTM Forecast Plot
- **Where**: Forecast tab > LSTM
- **What**: Historical vs 30-day future prediction
- **Why**: Predicts future stock price using deep learning

- ![LSTM Forecast Plot](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/LSTM%20forecast.png)

### 3. 🔢 ARIMA Forecast Plot
- **Where**: Forecast tab > ARIMA
- **What**: Historical + ARIMA prediction
- **Why**: Statistical trend comparison with LSTM

- ![ARIMA Forecast Plot](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/ARIMA%20plot.png)

### 4. 📉 Bollinger Bands
- **Where**: Indicators tab
- **What**: MA20 + upper/lower bands + closing price
- **Why**: Detects volatility and price range

- ![Bollinger Bands](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/Bollinger%20bands%20plot.png)

### 5. 📊 RSI (Relative Strength Index)
- **Where**: Indicators tab
- **What**: RSI line ranging 0–100
- **Why**: Highlights overbought or oversold signals

### 6. 📉 MACD (Moving Average Convergence Divergence)
- **Where**: Indicators tab
- **What**: MACD and signal line
- **Why**: Tracks price momentum and buy/sell signals

- ![RSI and MACD plot](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/RSI%20%26%20MACD.png)

### 7. 📈 Evaluation Plot
- **Where**: Evaluation tab
- **What**: Predicted vs Actual prices (LSTM)
- **Why**: Showcases model accuracy and performance

- ![Actual vs Predicted](https://github.com/Patel-Riya-D/Projects/blob/main/Stock_price_prediction/Evaluation%20plot.png)

---

## 🧠 AI Assistant
- Integrated chatbot using OpenAI for answering stock-related queries

---


## ✅ Future Enhancements

- 📥 Export to PDF/CSV
- 📊 Candlestick toggle
- 🔍 Advanced filters/sorting
- 🧮 More indicators like EMA, OBV, Volume
- 🔐 User login & preferences

---

## 🛠 How to Run

```bash
streamlit run stock.py
```

The dashboard will launch in your browser at `http://localhost:8501`.

---


