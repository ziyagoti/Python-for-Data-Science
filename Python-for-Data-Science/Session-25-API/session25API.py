#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-25 

import requests
import json
import time
import schedule


# Task 1: Fetch & Save Raw JSON

def fetch_crypto_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"

    try:
        res = requests.get(url, timeout=10)

        if res.status_code == 429:
            print("Rate limit hit. Retrying..")
            time.sleep(5)
            return fetch_crypto_data()

        if res.status_code != 200:
            print("API Error:", res.status_code)
            return []

        data = res.json()

        if not data:
            print("No data received")
            return []

        crypto = data[:10]

        with open("crypto_data.json", "w") as f:
            json.dump(crypto, f, indent=4)

        print("Data saved successfully")

        return crypto

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        return []

#Output:
#Data saved successfully


# Task 2: Find Most Volatile Coin

def find_most_volatile_coin(data):
    if not data:
        print("No data for volatility check")
        return

    max_change = 0
    volatile_coin = ""

    for coin in data:
        change = abs(float(coin.get("priceChangePercent", 0)))

        if change > max_change:
            max_change = change
            volatile_coin = coin["symbol"]

    print("Most Volatile Coin:", volatile_coin, "| Change:", max_change)

#Output:
#Most Volatile Coin: NEOBTC | Change: 16.659


# Task 3: Coins Below Average Price

def below_average_price(data):
    if not data:
        print("No data for price analysis")
        return

    prices = [float(coin["lastPrice"]) for coin in data]
    avg_price = sum(prices) / len(prices)

    print("Average Price:", avg_price)

    print("Coins below average price:")

    for coin in data:
        price = float(coin["lastPrice"])
        if price < avg_price:
            print(coin["symbol"], ":", price)

#Output:
#Coins below average price:
#LTCBTC : 0.000683
#NEOBTC : 3.542e-05
#QTUMETH : 0.0004655
#EOSETH : 0.0003067
#SNTETH : 1.7e-05
#BNTETH : 0.0002026
#BCCBTC : 0.0
#GASBTC : 2.07e-05


# Task 4: Rank Coins by Volume

def rank_coins_by_volume(data):
    if not data:
        print("No data for ranking")
        return

    sorted_coins = sorted(
        data,
        key=lambda x: float(x.get("quoteVolume", 0)),
        reverse=True
    )

    limit = min(5, len(sorted_coins))

    for i in range(limit):
        coin = sorted_coins[i]
        print(i + 1, coin["symbol"], "| Volume:", coin["quoteVolume"])

#Output:
#1 ETHBTC | Volume: 198.56615797
#2 QTUMETH | Volume: 163.57504584
#3 SNTETH | Volume: 160.35207145
#4 EOSETH | Volume: 117.17343445
#5 BNBBTC | Volume: 110.55067256


# Task 5: Automate Hourly Script with Error Handling

def job():
    print("\nRunning Crypto Tracker Job..\n")

    data = fetch_crypto_data()

    if data:
        find_most_volatile_coin(data)
        below_average_price(data)
        rank_coins_by_volume(data)


job()
schedule.every(1).hours.do(job)

print("\nScheduler started (runs every 1 hour)...")

while True:
    schedule.run_pending()
    time.sleep(1)

#Output:
#Running Crypto Tracker Job..

#Data saved successfully
#Most Volatile Coin: NEOBTC | Change: 16.659
#Average Price: 0.003807592
#Coins below average price:
#LTCBTC : 0.000683
#NEOBTC : 3.542e-05
#QTUMETH : 0.0004655
#EOSETH : 0.0003067
#SNTETH : 1.7e-05
#BNTETH : 0.0002026
#BCCBTC : 0.0
#GASBTC : 2.07e-05
#1 ETHBTC | Volume: 198.56615797
#2 QTUMETH | Volume: 163.57504584
#3 SNTETH | Volume: 160.35207145
#4 EOSETH | Volume: 117.17343445
#5 BNBBTC | Volume: 110.55067256

#Scheduler started (runs every 1 hour)...
