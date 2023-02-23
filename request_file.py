import requests
import json
import os

url = "http://localhost:5000/predict"

file_path = "./Dataset/Bed/Aubree Queen Bed.jpg"
with open(file_path, "rb") as f:
    file_content = f.read()

payload = {"file": (os.path.basename(file_path), file_content)}
headers = {}

response = requests.post(url, headers=headers, files=payload)

print(response.text)