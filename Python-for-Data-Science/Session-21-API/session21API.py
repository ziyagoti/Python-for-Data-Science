#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-21 (APIs Part 2)


import requests
import csv
import json


# Task 1
# POST request with JSON payload

url1 = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My API Post",
    "body": "Learning Python APIs",
    "userId": 10
}

res1 = requests.post(url1, json=payload)

print("Status Code:", res1.status_code)
print(res1.json())

# Output:
# 201
#{'title': 'My API Post', 'body': 'Learning Python APIs', 'userId': 10, 'id': 101}


# Task 2
# User input POST request

playlist_name = input("Enter playlist name: ")
playlist_desc = input("Enter description: ")

data = {
    "title": playlist_name,
    "body": playlist_desc,
    "userId": 1
}

res2 = requests.post(url1, json=data)

print("Playlist ID:", res2.json().get("id"))

# Output:
#Enter playlist name: chill songs
#Enter description: relax music
#Playlist ID: 101

# Task 3
# reqres API POST

url2 = "https://reqres.in/api/users"

user_data = {
    "name": "ziya",
    "job": "student"
}

res3 = requests.post(url2, json=user_data)

data3 = res3.json()

print("User ID:", data3.get("id"))
print("Created At:", data3.get("createdAt"))

# Output:
# User ID: None
# Created At: None


# Task 4
# Save API data to CSV

res4 = requests.get(url1)
posts = res4.json()[:5]

with open("posts.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["title", "userId"])

    for post in posts:
        writer.writerow([post["title"], post["userId"]])

print("CSV file created")

# Output:
# CSV file created


# Task 5
# Save API data to JSON

res5 = requests.get(url1)
posts5 = res5.json()[:5]

with open("posts.json", "w") as file:
    json.dump(posts5, file, indent=4)

print("JSON file created")

# Output:
# JSON file created