from flask import Flask
from nltk.sentiment import SentimentIntensityAnalyzer
import json
app = Flask("Sentiment Analyzer")

sia = SentimentIntensityAnalyzer()


@app.get('/')
def home():
    return "Welcome to the Sentiment Analyzer. \
    Use /analyze/text to get the sentiment"


@app.get('/analyze/<input_txt>')
def analyze_review_sentiments(input_txt):
    scores = sia.polarity_scores(input_txt)

    pos = float(scores['pos'])
    neg = float(scores['neg'])
    neu = float(scores['neu'])

    sentiment = "positive"

    if neg > pos and neg > neu:
        sentiment = "negative"
    elif neu > neg and neu > pos:
        sentiment = "neutral"

    return {"sentiment": sentiment}


if __name__ == "__main__":
    app.run(debug=True)
