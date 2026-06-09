#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-20 (APIs Part 1)


import requests


# Task 1
# GET posts + status code + first title

url1 = "https://jsonplaceholder.typicode.com/posts"

res1 = requests.get(url1)

print("Status Code:", res1.status_code)

data1 = res1.json()

print("First Title:", data1[0]["title"])

# Output:
# Status Code: 200
# First Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit


# Task 2
# POST request

data_post = {
    "title": "My First Post",
    "body": "Hello from Python!",
    "userId": 101
}

res2 = requests.post(url1, json=data_post)

print("Status Code:", res2.status_code)
print(res2.json())

# Output:
# 201
#{'title': 'My First Post', 'body': 'Hello from Python!', 'userId': 101, 'id': 101}


# Task 3
# Filter users with .org email

url2 = "https://jsonplaceholder.typicode.com/users"

res3 = requests.get(url2)

users = res3.json()

for user in users:
    if user["email"].endswith(".org"):
        print(user["username"])

# Output:
#Karianne

# Task 4
# OMDB API with params

url3 = "http://www.omdbapi.com/"

params = {
    "apikey": "demo",
    "s": "Avengers"
}

res4 = requests.get(url3, params=params)

data4 = res4.json()

print("Total Results:", data4.get("totalResults"))

# Output:
#Total Results: None
