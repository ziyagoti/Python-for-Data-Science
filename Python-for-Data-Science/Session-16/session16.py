#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-16

# Task 1
# iter() and next() with food apps

apps = ["Zomato", "Swiggy", "Dominos", "Blinkit", "Uber Eats"]

it = iter(apps)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Output:
# Zomato
# Swiggy
# Dominos
# Blinkit
# Uber Eats


# Task 2
# Generator function for playlist

def playlist_generator(songs):
    for song in songs:
        yield song

songs = ["Song A", "Song B", "Song C"]

gen = playlist_generator(songs)

print(next(gen))
print(next(gen))
print(next(gen))

# Output:
# Song A
# Song B
# Song C


# Task 3
# enumerate simple (without i, item loop style)

cart = ["Pizza", "Burger", "Fries", "Coke"]

i = 1
for item in cart:
    print(i, item)
    i = i + 1

# Output:
# 1 Pizza
# 2 Burger
# 3 Fries
# 4 Coke


# Task 4
# zip for teams and points

teams = ["MI", "CSK", "RCB"]
points = [18, 16, 14]

i = 0
while i < len(teams):
    print("Team:", teams[i], ", Points:", points[i])
    i = i + 1

# Output:
# Team: MI , Points: 18
# Team: CSK , Points: 16
# Team: RCB , Points: 14


# Task 5
# Generator for order IDs

def order_id_generator():
    order_id = 1001
    while True:
        yield order_id
        order_id = order_id + 1

gen = order_id_generator()

print(next(gen))
print(next(gen))
print(next(gen))

# Output:
# 1001
# 1002
# 1003