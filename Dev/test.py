import requests

BASE = "http://127.0.0.1:5000/"

data = [{"User_ID": 1, "Quiz_ID": "Yo1"},
        {"User_ID": 2, "Quiz_ID": "Yo2"},
        {"User_ID": 3, "Quiz_ID": "Yo3"},
        {"User_ID": 4, "Quiz_ID": "Yo4"}]

for i in range(len(data)):
    response = requests.put(BASE + "form/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + "form/2")
print(response.json())