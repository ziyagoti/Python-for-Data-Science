#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-6

# Task 1
# Create dictionary of Instagram followers

insta_followers = {
    "user1": 12000,
    "user2": 25000,
    "user3": 18000,
    "user4": 50000,
    "user5": 32000
}

print("Instagram Followers:", insta_followers)

# Output:
# Instagram Followers: {'user1': 12000, 'user2': 25000, 'user3': 18000, 'user4': 50000, 'user5': 32000}


# Task 2
# Add, update, and delete items in dictionary

insta_followers["user6"] = 15000          # add new
insta_followers["user2"] = 30000          # update
del insta_followers["user3"]              # delete 

print("Updated Instagram Followers:", insta_followers)

# Output:
# Updated Instagram Followers: {'user1': 12000, 'user2': 30000, 'user4': 50000, 'user5': 32000, 'user6': 15000}


# Task 3
# Display food items costing more than 200

food_prices = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 300,
    "Sandwich": 120,
    "Biryani": 280
}

print("Items above ₹200:")

for item in food_prices:
    if food_prices[item] > 200:
        print(item)

# Output:
# Items above ₹200:
# Pizza
# Pasta
# Biryani


# Task 4
# Set intersection example

flipkart_users = {"A", "B", "C", "D", "E"}
myntra_users = {"C", "D", "E", "F", "G"}

common_users = flipkart_users.intersection(myntra_users)

print("Common Users:", common_users)

# Output:
# Common Users: {'C', 'D', 'E'}


# Task 5
# Function for union of two playlists

def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

playlist1 = {"Arijit", "Shreya", "Badshah"}
playlist2 = {"Arijit", "Atif", "Neha"}

print("Unique Artists:", get_unique_artists(playlist1, playlist2))

# Output:
# Unique Artists: {'Arijit', 'Shreya', 'Badshah', 'Atif', 'Neha'}