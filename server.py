from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initialize Flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Retrieve the text to analyze from the GET request
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the sentiment_analyzer function to analyze the text
    response = sentiment_analyzer(text_to_analyze)

    # Assuming response is in JSON format, extract label and score
    response_json = eval(response)  # Convert string to dict if needed
    label = response_json['document']['label']
    score = response_json['document']['score']

    # Return a formatted string with the sentiment label and score
    return "The given text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
