from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

UPLOADS_DIR = "uploads"

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOADS_DIR, filename))
    sentiment_results = analyze_sentiment(filename)
    return jsonify(sentiment_results)

if __name__ == "__main__":
    app.run(debug=True)