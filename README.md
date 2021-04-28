# 中期答辩

## Tutorial

Reference: https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html
## 工作流

*Last Edited Apr 28,2021 by Andy*

WW上传一张图片
CYN这边接收保存
给ZM一个文件系统的地址
ZM返回一个list包括类别(数字)和一个图片地址(热力图)
CYN将ZM返回的数据打包发回WW

## back-end

### 服务器运维

运行服务器
- linux 
```
export FLASK_APP=app.py
flask run #公开访问 --host=0.0.0.0
```
- windows
```
set FLASK_APP=app.py #CMD
python -m flask run #公开访问 --host=0.0.0.0
```

后端API
`http://ip:5000/predict`
### 目前功能

- 接收前端POST来的一张图片
- 随机生成一个图片名 保存在 /temp_save
- 将图片url传给util.py的temp_func(), 获取病例类别int和热力图url
- 病例类别传给util.py的class_transf(), 获取病例名
- 将热力图转成base64字节流再转成字符流(utf-8)
- 将病例名和热力图字符流打包在json里传给前端
