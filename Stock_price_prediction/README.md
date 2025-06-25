
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

## 📷 Preview

### 🌐 Overview
Displays real-time stock info in stylish glassmorphism cards.

### 📈 Forecast Tab
Switch between LSTM and ARIMA model predictions with smooth Plotly animations and AI-generated summaries.

### 📉 Indicators
Visualize technical indicators like Bollinger Bands, RSI, and MACD.

### 📰 News Feed
Live headlines from financial markets with time and external links.

### 💬 Ask AI
Ask anything about stocks, models, or performance — get instant smart replies using OpenAI GPT.

---

## 📊 Visualizations & Plots

### 1. 📈 Mini Line Charts in Overview
- **Where**: On each stock card
- **What**: Past 30-day closing prices
- **Why**: Snapshot of stock momentum

### 2. 🔮 LSTM Forecast Plot
- **Where**: Forecast tab > LSTM
- **What**: Historical vs 30-day future prediction
- **Why**: Predicts future stock price using deep learning

### 3. 🔢 ARIMA Forecast Plot
- **Where**: Forecast tab > ARIMA
- **What**: Historical + ARIMA prediction
- **Why**: Statistical trend comparison with LSTM

### 4. 📉 Bollinger Bands
- **Where**: Indicators tab
- **What**: MA20 + upper/lower bands + closing price
- **Why**: Detects volatility and price range

### 5. 📊 RSI (Relative Strength Index)
- **Where**: Indicators tab
- **What**: RSI line ranging 0–100
- **Why**: Highlights overbought or oversold signals

### 6. 📉 MACD (Moving Average Convergence Divergence)
- **Where**: Indicators tab
- **What**: MACD and signal line
- **Why**: Tracks price momentum and buy/sell signals

### 7. 📈 Evaluation Plot
- **Where**: Evaluation tab
- **What**: Predicted vs Actual prices (LSTM)
- **Why**: Showcases model accuracy and performance

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

## 📌 Credits

- UI Inspired by: TradingView, Groww, and modern fintech designs  
- Data from: Yahoo Finance via `yfinance`, NewsAPI  
- Built using: `Streamlit`, `Plotly`, `Pandas`, `TensorFlow`, `OpenAI GPT`

