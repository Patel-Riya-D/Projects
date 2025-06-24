# chatbot.py

import streamlit as st

def simple_bot(user_input):
    responses = {
        "hello": "Hi there! 👋 How can I assist you with your stocks today?",
        "hi": "Hey! Ready to dive into some stock trends?",
        "hey": "Hello! Need help reading charts or predictions?",
        "forecast": "The forecast uses LSTM to analyze past stock data and predict future trends 📈.",
        "help": "You can choose a stock, view its indicators, and check out the prediction tab.",
        "indicators": "We show indicators like RSI and moving averages to help interpret stock momentum.",
        "prediction": "The prediction model uses past closing prices to estimate short-term movement.",
        "about model": "The LSTM model is trained on historical stock data and fine-tuned for short-term trends.",
        "stock price": "Just select a stock from the dropdown to view its live data and predictions.",
        "thank you": "You're welcome! I'm always here to assist 📊",
        "bye": "Goodbye! Happy trading and see you again soon 👋",
    }
    return responses.get(user_input.lower(), "Hmm, I'm not sure how to respond to that. Try 'help' or ask about the forecast.")

def show():
    st.title("💬 Chat with your Stock Assistant")
    st.write("I'm your simple chatbot — fast, focused, and here to help with your dashboard!")

    user_input = st.text_input("You:", placeholder="Type something like 'forecast' or 'indicators'")

    if user_input:
        response = simple_bot(user_input)
        st.markdown(f"**Bot:** {response}")
