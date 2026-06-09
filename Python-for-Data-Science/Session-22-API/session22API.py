#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-22 (Advanced APIs)


import requests
import asyncio
import httpx
#pip install httpx

# Task 1
# Session usage

s = requests.Session()

url = "https://jsonplaceholder.typicode.com/users/1"

r1 = s.get(url)
r2 = s.get(url)

print("Request 1:", r1.status_code)
print("Request 2:", r2.status_code)

# Output:
# Request 1: 200
# Request 2: 200


# Task 2
# OpenWeatherMap API

city = "Ahmedabad"
api_key = "YOUR_API_KEY"

weather_url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

w = requests.get(weather_url, params=params)
data = w.json()

if "main" in data:
    print("Temperature:", data["main"]["temp"])
else:
    print("Weather API Error:",data.get("message"))

# Output:
# Weather API Error: Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.


# Task 3
# Async fetch using httpx

async def fetch_data():
    async with httpx.AsyncClient() as client:

        task1 = client.get("https://jsonplaceholder.typicode.com/posts")
        task2 = client.get("https://jsonplaceholder.typicode.com/users")

        res1, res2 = await asyncio.gather(task1, task2)

        print("Posts status:", res1.status_code)
        print("Users status:", res2.status_code)

asyncio.run(fetch_data())

# Output:
# Posts status: 200
# Users status: 200


# Task 4
# Bearer token example

def get_user_profile():
    headers = {
        "Authorization": "Bearer fake_token_123"
    }

    res = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        headers=headers
    )

    data = res.json()
    print("User Name:", data["name"])

get_user_profile()

# Output:
# User Name: Leanne Graham


# Task 5
# OAuth URL generation (Spotify example)

client_id = "your_client_id"
redirect_uri = "http://localhost:8888/callback"

auth_url = (
    "https://accounts.spotify.com/authorize"
    f"?client_id={client_id}"
    f"&response_type=code"
    f"&redirect_uri={redirect_uri}"
    f"&scope=user-read-private"
)

print("OAuth URL:", auth_url)

# Output:
#OAuth URL: https://accounts.spotify.com/authorize?client_id=your_client_id&response_type=code&redirect_uri=http://localhost:8888/callback&scope=user-read-private