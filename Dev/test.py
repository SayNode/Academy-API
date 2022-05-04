import requests

BASE = "http://127.0.0.1:5000/"

data = [{"UI": "1Yo1","User_ID": "1", "Quiz_ID": "Yo1", "Reward": 0, "Completed": False},
        {"UI": "2Yo2","User_ID": "2", "Quiz_ID": "Yo2", "Reward": 0, "Completed": False},
        {"UI": "3Yo3","User_ID": "3", "Quiz_ID": "Yo3", "Reward": 0, "Completed": False},
        {"UI": "4Yo4","User_ID": "4", "Quiz_ID": "Yo4", "Reward": 0, "Completed": False}]

for i in range(len(data)):
    form_ID = data[i]["User_ID"] + data[i]["Quiz_ID"]
    #We store this info in base + "The user ID" +"/"+ "the formID". This way its easy to query what each user has done
    #print(BASE + "form/"+data[i]["User_ID"]+"/" + form_ID, data[i])
    response = requests.put(BASE +"form/" + form_ID, data[i])
    print(response.json())

input()

response = requests.get(BASE + "form/2Yo2")
print(response.json())