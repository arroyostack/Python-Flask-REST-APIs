import requests
#  pip3 install requests  
BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + "video/1", {"likes": 10})
# print(response.json())
# This request was sent on purpose with two arguments missing ====> {'1': {'name': None, 'views': None, 'likes': 10}}
# It did not throw an error because the parameters were not specified as required. 
# If specified as required it will send the message we have attached to the help attribute
data = [
    {"likes": 10, "name": "Hommer sings in Moe Bar", "views": 476983},
    {"likes": 10827, "name": "Marge become a politician", "views": 439847},
    {"likes": 276830, "name": "Lisa plays at a jam session", "views": 5674845},
    {"likes": 93020, "name": "Bart calls Moe bar once again", "views": 98379743}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
    
input()

response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/0")
print(response.json())