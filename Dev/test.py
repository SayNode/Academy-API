import requests

BASE = "http://127.0.0.1:5000/"

input()

response = requests.get(BASE + "form/0x873648292jei283/32")
print(response.json())