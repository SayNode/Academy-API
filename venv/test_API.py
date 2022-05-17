import requests
import curlify
#BASE = "http://127.0.0.1:5000/"
BASE = "http://rewardapi-env.eba-p9wphyaq.us-east-1.elasticbeanstalk.com/"
user_wallet = "0x306a430f0e361e96e69d650067eba3f73307b5c4"
rewards = 0.1

response = requests.get(BASE + "form/" + user_wallet+"/" +str(rewards))
print(curlify.to_curl(response.request)) 
print(response.json())