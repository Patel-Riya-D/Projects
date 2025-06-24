import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def run_arima(ticker, forecast_days=30):
    df = yf.Ticker(ticker).history(period='1y')

    if df.empty or 'Close' not in df.columns:
        fig = go.Figure().add_annotation(text="⚠️ No data available")
        return fig, None, None, None

    close = df['Close'].dropna()
    train = close[:-forecast_days]
    test = close[-forecast_days:]

    try:
        model = ARIMA(train, order=(5, 1, 0)).fit()
        forecast = model.forecast(steps=forecast_days)
        future_dates = pd.date_range(start=close.index[-1] + pd.Timedelta(days=1), periods=forecast_days)

        # Metrics
        mae = mean_absolute_error(test, forecast)
        rmse = np.sqrt(mean_squared_error(test, forecast))
        accuracy = 100 - (mae / np.mean(test)) * 100

        # Plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=close.index, y=close, name='Historical'))
        fig.add_trace(go.Scatter(x=future_dates, y=forecast, name='ARIMA Forecast', line=dict(color="orange")))
        fig.update_layout(title="ARIMA Forecast", template="plotly_dark")

        return fig, accuracy, mae, rmse
    except Exception as e:
        fig = go.Figure().add_annotation(text=f"❌ ARIMA failed: {e}")
        return fig, None, None, None
