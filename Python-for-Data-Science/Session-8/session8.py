#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-8

# Task 1
# Print favorite apps using for loop

apps = ["Zomato", "Swiggy", "Dominos", "Blinkit", "Uber Eats"]

for app in apps:
    print(app)

# Output:
# Zomato
# Swiggy
# Dominos
# Blinkit
# Uber Eats


# Task 2
# While loop for first day > 10000 steps

steps = [8000, 9500, 12000, 7000, 11000, 9000]

i = 0

while i < len(steps):
    if steps[i] > 10000:
        print("Crossed 10000 steps:", steps[i])
        break
    i = i + 1

# Output:
# Crossed 10000 steps: 12000


# Task 3
# IPL teams with continue

teams = ["CSK", "MumbaiIndians", "RCB", "KKR", "GT"]

for team in teams:
    if len(team) <= 6:
        continue
    print(team)

# Output:
# MumbaiIndians


# Task 4
# enumerate song durations

songs = [210, 180, 240, 200]

i = 1

for duration in songs:
    print("Song", i, ":", duration, "seconds")
    i = i + 1

# Output:
# Song 1 : 210 seconds
# Song 2 : 180 seconds
# Song 3 : 240 seconds
# Song 4 : 200 seconds


# Task 5
# Shopping cart total with break and continue

prices = [500, 0, 700, 900, 300, 400]

total = 0

for price in prices:
    if price == 0:
        continue
    total += price
    if total > 2000:
        break
    total += price

print("Final Total:", total)

# Output:
# Final Total: 2000