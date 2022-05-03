import requests

BASE = "http://127.0.0.1:5000/"

requests.put(BASE + "video/1", {"name":"yomama", "views": 234, "likes": 34})
requests.put(BASE + "video/2", {"name":"yomama2", "views": 2, "likes": 2})
requests.put(BASE + "video/3", {"name":"yomama3", "views": 3, "likes": 3})
response = requests.get(BASE + "video/1")
print(response.json())