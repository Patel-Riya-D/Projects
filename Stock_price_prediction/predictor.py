import yfinance as yf
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
import plotly.graph_objects as go

def predict_lstm(ticker, forecast_days=30):
    df = yf.Ticker(ticker).history(period='2y')
    close = df['Close'].dropna().values.reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(close)

    X = []
    y = []
    for i in range(60, len(scaled)):
        X.append(scaled[i-60:i, 0])
        y.append(scaled[i, 0])
    X = np.array(X).reshape(-1, 60, 1)
    y = np.array(y).reshape(-1, 1)

    # Model Architecture
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(60, 1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    model.load_weights(f"models/{ticker.lower()}_weights.h5")

    preds = model.predict(X)
    inv_preds = scaler.inverse_transform(preds)
    inv_y = scaler.inverse_transform(y)

    # Metrics
    mae = mean_absolute_error(inv_y, inv_preds)
    rmse = np.sqrt(mean_squared_error(inv_y, inv_preds))
    accuracy = 100 - (mae / np.mean(inv_y)) * 100
    metrics = {"accuracy": accuracy, "mae": mae, "rmse": rmse}

    # Forecast for future days (optional)
    future_dates = pd.date_range(start=df.index[-1], periods=len(inv_preds)+1, freq='D')[1:]
    forecast_df = pd.DataFrame({'Date': future_dates, 'Forecast': inv_preds.flatten()})

    # Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index[-len(inv_preds):], y=inv_y.flatten(), name="Historical"))
    fig.add_trace(go.Scatter(x=future_dates, y=inv_preds.flatten(),
                             name="LSTM Forecast", line=dict(color='orange')))
    fig.update_layout(title="LSTM Forecast", template="plotly_dark")

    trend = "Expected to rise 📈" if inv_preds[-1] > inv_y[-1] else "Might fall 📉"

    return fig, metrics, trend, inv_y.flatten().tolist(), inv_preds.flatten().tolist()
