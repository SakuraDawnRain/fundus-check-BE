from flask import Flask, jsonify, request
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/')
@cross_origin()
def hello():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    file = request.files['file']
    bytes = file.read()
    result = {
        'class_name': 'Cataract',
        'precision': '0.9'
    }
    return jsonify(result)
