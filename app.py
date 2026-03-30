from flask import Flask, request, jsonify
from model import analyze_sentiment
from detector import detect_language

app = Flask(__name__)

@app.route("/")
def home():
    return "Multilingual Sentiment Analyzer API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]

    if not isinstance(text, str) or text.strip() == "":
        return jsonify({"error": "Invalid text input"}), 400

    language = detect_language(text)
    sentiment_result = analyze_sentiment(text)

    return jsonify({
        "text": text,
        "language": language,
        **sentiment_result
    })

if __name__ == "__main__":
    app.run(debug=True)