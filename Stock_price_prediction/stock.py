import streamlit as st
import forecast
import overview_panel
import indicators
import news_panel
import evaluation
import chatbot

def load_css():
    try:
        with open("styles/style.css", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ styles.css not found.")
    except UnicodeDecodeError:
        st.error("❌ Unable to decode styles.css. Please save it with UTF-8 encoding.")

def main():
    st.set_page_config(
        page_title="📈 Tracker — AI Stock Dashboard",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    load_css()

    # 📈 Tracker inline heading
    st.markdown("""
    <div class="tracker-title">
        📈 Tracker — <span style="opacity: 0.8;">AI Stock Dashboard</span>
    </div>
    """, unsafe_allow_html=True)

    # Optional large header below (if needed)
    # st.markdown("<h1 style='font-family:Poppins, sans-serif;'>💹 AI-Powered Stock Dashboard</h1>", unsafe_allow_html=True)

    # Sidebar Tabs
    tabs = [
        "📦 Overview",
        "📈 Forecast",
        "📉 Indicators",
        "📰 News",
        "📊 Evaluation",
        "💬 Ask AI"
    ]

    selected_index = tabs.index(st.session_state.get("tab", tabs[0]))
    tab = st.sidebar.radio("🌐 Navigation", tabs, index=selected_index)
    st.session_state["tab"] = tab

    # Show active tab content
    try:
        if tab == "📦 Overview":
            overview_panel.show()
        elif tab == "📈 Forecast":
            forecast.show()
        elif tab == "📉 Indicators":
            indicators.show()
        elif tab == "📰 News":
            news_panel.show()
        elif tab == "📊 Evaluation":
            evaluation.show()
        elif tab == "💬 Ask AI":
            chatbot.show()
    except Exception as e:
        st.error(f"⚠️ Error loading the '{tab}' section:\n\n{e}")

if __name__ == "__main__":
    main()
