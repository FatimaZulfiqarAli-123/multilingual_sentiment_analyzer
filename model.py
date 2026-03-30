from transformers import pipeline

print("DEBUG: model.py loaded")

# ✅ Better multilingual sentiment model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-xlm-roberta-base-sentiment"
)

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]

    label = result["label"].lower()
    score = result["score"]

    # Normalize sentiment labels safely
    if "positive" in label:
        sentiment = "Positive"
    elif "negative" in label:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "confidence": round(float(score), 3)
    }