from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from AI import make_gemini_request

app = Flask(__name__)
CORS(app)
data=""

@app.route('/')
def home():
    return render_template('index.html')    # render index.html

@app.route('/submit', methods=['POST'])  
def submit():
    # get the data from the form
    data=""
    data = request.get_json()
    if not data or 'inputText' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    userMessage = data['inputText']
    response = make_gemini_request(userMessage)
    if hasattr(response, 'text'):  # Ensure response has a 'text' attribute
        return jsonify({'response': response.text})






