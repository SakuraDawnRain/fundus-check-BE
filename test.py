import requests

url = "http://127.0.0.1:5000/predict"
files = {
    'file': (open("imed.png", 'rb'))
}
r = requests.post(url, files=files)

print(r.content)
