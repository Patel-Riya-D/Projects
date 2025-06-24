import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

def get_index_change(ticker):
    try:
        data = yf.Ticker(ticker).history(period="2d")
        if len(data) < 2:
            return None
        prev_close = data["Close"].iloc[-2]
        latest = data["Close"].iloc[-1]
        change = ((latest - prev_close) / prev_close) * 100
        return round(change, 2)
    except Exception:
        return None

def show():
    # Fetch live index % changes
    nasdaq = get_index_change("^IXIC")
    sp500 = get_index_change("^GSPC")
    sensex = get_index_change("^BSESN")

    def style_pct(val):
        if val is None:
            return "<span style='color:#aaa;'>N/A</span>"
        color = "#28e07c" if val > 0 else "#ff5f5f" if val < 0 else "#f1c40f"
        return f"<span style='color:{color};'>{val:+.2f}%</span>"

    st.markdown(f"""
    <div style='background: rgba(255,255,255,0.08); padding: 10px 15px; border-radius: 10px;
                margin-bottom: 25px; text-align:center; font-weight:500; font-size:14px;'>
        🌍 NASDAQ {style_pct(nasdaq)} &nbsp;&nbsp; | &nbsp;&nbsp;
        S&P 500 {style_pct(sp500)} &nbsp;&nbsp; | &nbsp;&nbsp;
        Sensex {style_pct(sensex)}
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📦 Stock Overview")

    tickers = {
        "AAPL": "Apple",
        "MSFT": "Microsoft",
        "GOOGL": "Alphabet",
        "AMZN": "Amazon",
        "META": "Meta"
    }

    cols = st.columns([1, 1, 1])

    for i, (symbol, name) in enumerate(tickers.items()):
        with cols[i % 3]:
            try:
                ticker = yf.Ticker(symbol)
                df = ticker.history(period="3mo", interval="1d")
                info = ticker.info
                close = df["Close"].ffill()

                if len(close) < 20:
                    continue

                latest = close.iloc[-1]
                prev = close.iloc[-2]
                pct = round((latest - prev) / prev * 100, 2)
                signal = "🟢 BUY" if pct > 1 else "🔴 SELL" if pct < -1 else "🟡 HOLD"

                pe = info.get("trailingPE", "N/A")
                beta = info.get("beta", "N/A")
                cap = info.get("marketCap", "N/A")
                rating = info.get("recommendationKey", "N/A").upper()

                st.image(f"styles/logos/{symbol}.png", width=60)

                st.markdown(f"""
                <div class="card" style="position: relative;">
                    <h4 style="margin-bottom:0.4rem;">{symbol} — {name}</h4>
                    <div class="metric-line">💰 ${latest:.2f} ({pct:+.2f}%) — <b>{signal}</b></div>
                    <div style="margin-bottom:0.5rem;">
                        <span class="pill">P/E: {pe}</span>
                        <span class="pill">Beta: {beta}</span>
                        <span class="pill">Cap: {cap:,}</span>
                        <span class="pill">Rating: {rating}</span>
                    </div>
                """, unsafe_allow_html=True)

                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=close.index[-30:],
                    y=close[-30:],
                    mode="lines+markers",
                    line=dict(color="#0dcaf0", width=3),
                    marker=dict(size=4, color="#0dcaf0"),
                    hovertemplate="%{y:.2f} on %{x|%b %d}"
                ))
                fig.update_layout(
                    height=160,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin=dict(l=0, r=0, t=10, b=10),
                    xaxis=dict(visible=False, showgrid=True, gridcolor='rgba(255,255,255,0.05)'),
                    yaxis=dict(visible=False, showgrid=True, gridcolor='rgba(255,255,255,0.05)')
                )

                st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False}, key=f"{symbol}_chart")
                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"{symbol}: {e}")
