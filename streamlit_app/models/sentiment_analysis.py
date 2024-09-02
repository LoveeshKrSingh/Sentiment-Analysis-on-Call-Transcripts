import pandas as pd
from transformers import pipeline

nlp = pipeline("sentiment-analysis")

def analyze_sentiment(filename):
    transcript = open(os.path.join("uploads", filename), "r").read()
    sentiment_results = nlp(transcript)
    return {
        "sentiment": sentiment_results[0]["label"],
        "score": sentiment_results[0]["score"]
    }