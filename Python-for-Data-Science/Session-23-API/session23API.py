#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-23 (API Mini Projects)



# Task 1: Weather API
import requests

API_KEY = "eacdfae384bbfd52334d9900b5f52da1"
city = "Ahmedabad"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("City:", city)
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
    else:
        print("API Error:", data["message"])

except Exception as e:
    print("Error:", e)

#Output:
#City: Ahmedabad
#Temperature: 33.03 °C
#Weather: few clouds

# Task 2: Crypto Prices

import requests
from datetime import datetime

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

response = requests.get(url)
data = response.json()

print("Date & Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
print("Bitcoin Price (USD):", data["bitcoin"]["usd"])
print("Ethereum Price (USD):", data["ethereum"]["usd"])

#Output:
#Date & Time: 09-06-2026 22:02:40
#Bitcoin Price (USD): 60998
#Ethereum Price (USD): 1629.19


# Task 3: NASA APOD

import requests

api_key = "DEMO_KEY"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
data = response.json()

print("Title:", data["title"])
print("\nExplanation:")
print(data["explanation"])

image_url = data["url"]

img = requests.get(image_url)

with open("nasa_apod.jpg", "wb") as file:
    file.write(img.content)

print("\nImage saved successfully as nasa_apod.jpg")

#Output:
#Title: Thor's Helmet

#Explanation:
#Thor not only has his own day (Thursday), but a helmet in the heavens.  Popularly called Thor's Helmet, NGC 2359 is a hat-shaped cosmic cloud with wing-like appendages. Heroically sized even for a Norse god, Thor's Helmet is about 30 light-years across. In fact, the cosmic head-covering is more like an interstellar bubble, blown by a fast wind from the bright, massive star near the bubble's center. Known as a Wolf-Rayet star, the central star is an extremely hot giant thought to be in a brief, pre-supernova stage of evolution. NGC 2359 is located about 15,000 light-years away toward the constellation of the Great Overdog. This sharp image is a combination of deep images taken in light emitted by hydrogen (red) and oxygen (blue).  The star in the center of Thor's Helmet is expected to explode in a spectacular supernova sometime within the next few thousand years.   Sky Surprise: What picture did APOD feature on your birthday? (after 1995)

#Image saved successfully as nasa_apod.jpg


# Task 4: COVID India Data

import requests

url = "https://disease.sh/v3/covid-19/countries/India"

response = requests.get(url)
data = response.json()

print("-" * 40)
print("{:<15} {:>15}".format("Metric", "Count"))
print("-" * 40)

print("{:<15} {:>15}".format("Cases", data["cases"]))
print("{:<15} {:>15}".format("Recovered", data["recovered"]))
print("{:<15} {:>15}".format("Deaths", data["deaths"]))

print("-" * 40)

#Output:
#----------------------------------------
#Metric                    Count
#----------------------------------------
#Cases                  45035393
#Recovered                     0
#Deaths                   533570
#----------------------------------------


# Task 5: Combined API

import requests

weather_status = "Unavailable"
bitcoin_status = "Unavailable"

# Weather API
try:
    API_KEY = "eacdfae384bbfd52334d9900b5f52da1"

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid={API_KEY}&units=metric"

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    if weather_response.status_code == 200:
        weather_status = f"{weather_data['main']['temp']} °C"
    else:
        weather_status = weather_data["message"]

except Exception as e:
    weather_status = str(e)

# Bitcoin API
try:
    crypto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    crypto_response = requests.get(crypto_url)
    crypto_data = crypto_response.json()

    bitcoin_status = f"${crypto_data['bitcoin']['usd']}"

except Exception as e:
    bitcoin_status = str(e)

print("===== Combined API Dashboard =====")
print("Mumbai Temperature :", weather_status)
print("Bitcoin Price      :", bitcoin_status)

#Output:
#===== Combined API Dashboard =====
#Mumbai Temperature : 31.04 °C
#Bitcoin Price      : $61017
