from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from AI import get_ai_response
from gethealthcare import get_healthcare_info

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')    # render index.html

@app.route('/submit', methods=['POST'])  
def submit():
    # get the data from the form    
    try:
        data = request.get_json()
        if not data or 'inputText' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        zip = data['inputText'].split(' ')[0]
        userMessage = data['inputText']
        response = get_ai_response(userMessage)
        if response.text.split(' ')[0] == "Sorry,":
            return jsonify({'response': response.text.strip("\n")})
        providers = get_healthcare_info(str(zip), response.text.strip("\n"))
        if hasattr(response, 'text'):  # Ensure response has a 'text' attribute
            return jsonify({'response': response.text.strip("\n") + "\n" + providers})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400







