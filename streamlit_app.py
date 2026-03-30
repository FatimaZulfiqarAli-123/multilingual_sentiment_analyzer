import streamlit as st
from model import analyze_sentiment
from detector import detect_language

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Multilingual Sentiment Analyzer",
    layout="centered"
)

# ---------------- BACKGROUND + UI STYLE ----------------
st.markdown("""
    <style>

    /* Background image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1557683316-973673baf926");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Dark overlay for readability */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.65);
        z-index: 0;
    }

    /* Keep content above overlay */
    .block-container {
        position: relative;
        z-index: 1;
    }

    /* Title */
    .title {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        color: #38bdf8;
        margin-bottom: 10px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #cbd5e1;
        margin-bottom: 30px;
    }

    /* Card box */
    .box {
        background: rgba(30, 41, 59, 0.85);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
        backdrop-filter: blur(6px);
    }

    .result {
        font-size: 18px;
        margin-top: 10px;
        color: white;
    }

    .positive {
        color: #22c55e;
        font-weight: bold;
    }

    .negative {
        color: #ef4444;
        font-weight: bold;
    }

    .neutral {
        color: #facc15;
        font-weight: bold;
    }

    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">Multilingual Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detect sentiment in any language using AI</div>', unsafe_allow_html=True)

# ---------------- INPUT ----------------
text = st.text_area("✍️ Enter your text", height=120)

analyze = st.button("🚀 Analyze Sentiment")

# ---------------- RESULTS ----------------
if analyze:
    if text.strip():

        lang = detect_language(text)
        result = analyze_sentiment(text)

        sentiment = result["sentiment"]
        confidence = result["confidence"]

        if sentiment == "Positive":
            color_class = "positive"
        elif sentiment == "Negative":
            color_class = "negative"
        else:
            color_class = "neutral"

        st.markdown("## 📊 Results")

        st.markdown(f"""
        <div class="box">
            <p class="result">🌐 Language: <b>{lang}</b></p>
            <p class="result">🎯 Sentiment: <span class="{color_class}">{sentiment}</span></p>
            <p class="result">📈 Confidence: <b>{confidence}</b></p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter some text")