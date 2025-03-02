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
        print (zip)
        userMessage = data['inputText']
        response = get_ai_response(userMessage)
        print (response.text)
        # providers = get_healthcare_info(zip, response.text)
        if hasattr(response, 'text'):  # Ensure response has a 'text' attribute
            return jsonify({'response': response.text})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400






