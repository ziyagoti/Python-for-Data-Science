#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-7

# Task 1
# Spotify listening time check

listening_time = 150

if listening_time > 120:
    print("You are a true music fan!")
else:
    print("Keep listening!")

# Output:
# You are a true music fan!


# Task 2
# Zomato order amount check

order_amount = int(input("Enter Zomato order amount: "))

if order_amount > 300:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")

# Output:
# Enter Zomato order amount: 250
# Delivery charges apply


# Task 3
# Flipkart discount logic

cart_total = int(input("Enter Flipkart cart total: "))

if cart_total > 2000:
    print("You get a 10% discount")
elif cart_total > 1000:
    print("You get a 5% discount")
else:
    print("No discount available")

# Output:
# Enter Flipkart cart total: 1500
# You get a 5% discount


# Task 4
# IPL fantasy points (nested if-else)

points = int(input("Enter IPL fantasy team points: "))

if points > 500:
    if points > 800:
        print("Champion")
    else:
        print("Top Performer")
else:
    print("Keep Trying")

# Output:
# Enter IPL fantasy team points: 900
# Champion