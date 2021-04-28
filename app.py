from flask import Flask, jsonify, request
from flask_cors import cross_origin
import os,random,string,base64
import util

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route('/')
@cross_origin()
def hello():
    return 'Hello, this IMED from SUSTech'

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    img = request.files['file']
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    path = basedir+"/temp_save/"
    imgName = ran_str+img.filename
    file_path = path+imgName
    img.save(file_path)
    classification,heatmap_url=util.temp_func(file_path)
    classification=util.class_transf(classification)
    with open(heatmap_url, 'rb') as f:
            heatmap_base64 = base64.b64encode(f.read())
    heatmap_base64=heatmap_base64.decode('utf-8')
    result = {
        'class_name': classification,
        'heatmap': heatmap_base64
    }
    return jsonify(result)
