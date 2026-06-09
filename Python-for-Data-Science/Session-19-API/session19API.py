#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-19 (APIs)


import requests
import json


# Task 1
# GET request and print first 5 post titles

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

for i in range(5):
    print(data[i]["title"])

# Output:
#sunt aut facere repellat provident occaecati excepturi optio reprehenderit
#qui est esse
#ea molestias quasi exercitationem repellat qui ipsa sit aut
#eum et est occaecati
#nesciunt quas odio

# Task 2
# Dictionary to JSON

restaurant = {
    "name": "Food Hub",
    "location": "Surat",
    "cuisines": "Indian, Chinese",
    "ratings": 4.3
}

json_data = json.dumps(restaurant)

print(json_data)

# Output:
#{"name": "Food Hub", "location": "Surat", "cuisines": "Indian, Chinese", "ratings": 4.3}


# Task 3
# POST request

new_playlist = {
    "title": "My Songs",
    "userId": 1,
    "body": "Top 5 Spotify tracks"
}

res = requests.post(url, json=new_playlist)

print(res.status_code)
print(res.json())

# Output:
# 201
# {'title': 'My Songs', 'userId': 1, 'body': 'Top 5 Spotify tracks', 'id': 101}


# Task 4
# GET with params (userId=2)

params = {"userId": 2}

res2 = requests.get(url, params=params)
data2 = res2.json()

for item in data2:
    print(item["id"])

# Output:
#11
#12
#13
#14
#15
#16
#17
#18
#19
#20

# Task 5
# Custom headers example

headers = {
    "Authorization": "Bearer demo_token_123"
}

res3 = requests.get(url, headers=headers)

print(res3.status_code)

# Output:
# 200