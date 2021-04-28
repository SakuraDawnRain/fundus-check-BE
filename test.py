import requests

url = "http://10.21.41.245:5000/predict"
files = {
    'file': (open("./temp_data_set/imed.png", 'rb'))
}
r = requests.post(url, files=files)

print(r.content)
