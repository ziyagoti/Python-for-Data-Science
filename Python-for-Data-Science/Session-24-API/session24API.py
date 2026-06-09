#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-24 (Crypto price tracker)

#Task1:
#Fetch Top 10 Cryptos

import requests
import csv

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

try:
    res = requests.get(url, params=params)

    if res.status_code == 200:
        data = res.json()

        print("--Top 10 Crypto Prices--")
        for coin in data:
            print(coin["name"], ":", coin["current_price"], "USD")

        # OUTPUT:
        # --Top 10 Crypto Prices--
        # Bitcoin : 62653 USD
        # Ethereum : 1676.2 USD
        # Tether : 0.999456 USD
        # BNB : 597.53 USD
        # USDC : 0.999679 USD
        # XRP : 1.16 USD
        # Solana : 66.26 USD
        # TRON : 0.322999 USD
        # Figure Heloc : 1.027 USD
        # Hyperliquid : 61.91 USD

# Task 2: Add Price Change %, High, Low

        print("\n--Extra Details--")
        for coin in data:
            print(coin["name"], "|", coin["price_change_percentage_24h"], "%")

        # OUTPUT:
        # --Extra Details--
        # Bitcoin | -0.60992 %
        # Ethereum | -0.15224 %
        # Tether | 0.02134 %
        # BNB | -0.36662 %
        # USDC | -0.01019 %
        # XRP | 0.76812 %
        # Solana | -0.07617 %
        # TRON | -1.19395 %
        # Figure Heloc | 2.19418 %
        # Hyperliquid | 0.39144 %


# Task 3: Save Data to CSV

        with open("crypto_prices.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Price", "Change %", "High", "Low"])

            for coin in data:
                writer.writerow([
                    coin["name"],
                    coin["current_price"],
                    coin["price_change_percentage_24h"],
                    coin["high_24h"],
                    coin["low_24h"]
                ])

        print("\nCSV file created")

        # OUTPUT:
        # CSV file created

    else:
        print("API Error")

        # OUTPUT:
        # API Error

# Task 4: Error Handling

except Exception as e:
    print("Error:", e)

    # OUTPUT:
    # Error: <message>