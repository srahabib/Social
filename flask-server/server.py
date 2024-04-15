from flask import Flask, jsonify, request
from textblob import TextBlob

app = Flask(__name__)

# Route to calculate polarity, subjectivity, and sentiment


@app.route("/analyze_text", methods=["POST"])
def analyze_text():
    # Get the text from the request data
    text = request.json.get("text")

    # Calculate polarity, subjectivity, and sentiment
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"

    # Return the scores as JSON
    return jsonify({
        "polarity": polarity,
        "subjectivity": subjectivity,
        "sentiment": sentiment
    })


if __name__ == "__main__":
    app.run(debug=True)
