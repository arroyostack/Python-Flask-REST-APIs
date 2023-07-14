import requests
#  pip3 install requests  
BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + "video/1", {"likes": 10})
# print(response.json())
# This request was sent on purpose with two arguments missing ====> {'1': {'name': None, 'views': None, 'likes': 10}}
# It did not throw an error because the parameters were not specified as required. 
# If specified as required it will send the message we have attached to the help attribute

# Now we have set the parameters as required in the put function at main.py
# response = requests.put(BASE + "video/1", {"likes": 10, "name": "Sally skating in Florida", "views": 100000})
# print(response.json())

response = requests.get(BASE + "video/5")
print(response.json())