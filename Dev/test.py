import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 1, "name": "Yo1", "views":1},
        {"likes": 2, "name": "Yo2", "views":2},
        {"likes": 3, "name": "Yo3", "views":3},
        {"likes": 4, "name": "Yo4", "views":4},]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + "video/2")
print(response.json())