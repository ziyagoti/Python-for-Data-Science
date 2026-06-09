#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-23 (API Mini Projects)


import requests
from datetime import datetime


# Task 1: Weather API
city = "Ahmedabad"
api_key = "YOUR_API_KEY"

weather_url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

res = requests.get(weather_url, params=params)
data = res.json()

print("\n--- Weather Info ---")

if "main" in data:
    print("City:", city)
    print("Temp:", data["main"]["temp"], "°C")
    print("Description:", data["weather"][0]["description"])
else:
    print("Weather Error:", data.get("message"))


# Task 2: Crypto Prices
crypto_url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "inr"
}

res = requests.get(crypto_url, params=params)
data = res.json()

print("\n--- Crypto Prices ---")
print("Date:", datetime.now())
print("Bitcoin:", data["bitcoin"]["inr"], "INR")
print("Ethereum:", data["ethereum"]["inr"], "INR")


# Task 3: NASA APOD
nasa_url = "https://api.nasa.gov/planetary/apod"

params = {
    "api_key": "DEMO_KEY"
}

res = requests.get(nasa_url, params=params)
data = res.json()

print("\n--- NASA APOD ---")
print("Title:", data["title"])
print("Explanation:", data["explanation"][:200], "...")

if data["media_type"] == "image":
    img = requests.get(data["url"]).content
    with open("nasa_image.jpg", "wb") as f:
        f.write(img)
    print("Image saved as nasa_image.jpg")


# Task 4: COVID India Data
covid_url = "https://disease.sh/v3/covid-19/countries/India"

res = requests.get(covid_url)
data = res.json()

print("\n--- COVID India ---")
print("Cases:", data["cases"])
print("Recovered:", data["recovered"])
print("Deaths:", data["deaths"])


# Task 5: Combined API
print("\n--- Combined Data ---")

try:
    weather = requests.get(weather_url, params=params).json()
    crypto = requests.get(crypto_url, params=params).json()

    print("City:", city)

    if "main" in weather:
        print("Temp:", weather["main"]["temp"], "°C")
    else:
        print("Weather Error:", weather.get("message"))

    print("Bitcoin:", crypto["bitcoin"]["inr"], "INR")

except:
    print("Error fetching APIs")