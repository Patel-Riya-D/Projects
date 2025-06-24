import streamlit as st
import feedparser
import random

def get_tag_emoji(title):
    title = title.lower()
    if "ai" in title:
        return "🤖"
    if "oil" in title or "energy" in title:
        return "🛢️"
    if "bank" in title or "finance" in title:
        return "💰"
    if "stock" in title or "market" in title:
        return "📈"
    return random.choice(["🔍", "📉", "💹", "🔮"])

def show():
    st.subheader("📰 Market News", anchor=False)
    feed = feedparser.parse("https://finance.yahoo.com/news/rssindex")

    for entry in feed.entries[:6]:
        title = entry.title
        published = entry.published
        link = entry.link
        tag = get_tag_emoji(title)

        st.markdown(f"""
            <div class="news-card">
                <h4>{tag} {title}</h4>
                <p style="font-size:13px; color:#bbb;">🕒 {published}</p>
                <a href="{link}" target="_blank">🔗 Read More</a>
            </div>
        """, unsafe_allow_html=True)
