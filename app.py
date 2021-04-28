from flask import Flask, jsonify, request,render_template
from flask_cors import cross_origin
import os,random,string,base64
import util

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route('/')
@cross_origin()
def hello():
    return render_template('Search.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    # 获取POST来的图片
    img = request.files['photo']
    # 产生随机图片名 存储到/temp_save/ 生成热力图的对应url
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    imgName = ran_str+'_'+img.filename
    path_save = basedir+"/temp_save/"
    path_heatmap = basedir+"/temp_heatmap"
    file_path_save = path_save+imgName
    file_path_heatmap = path_heatmap+imgName
    img.save(file_path_save)
    # 调取ZM的API 传图片url 获取类别int 获取类名和热力图字节流转字符流
    classification=util.temp_func(file_path_save,file_path_heatmap)
    with open(file_path_save, 'rb') as f:
            heatmap_base64 = base64.b64encode(f.read())
    heatmap_base64=heatmap_base64.decode('utf-8')
    # 打包进json 发回前端
    
    return render_template("Search.html",n=classification,u=heatmap_base64)
