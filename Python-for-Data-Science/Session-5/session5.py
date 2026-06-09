#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-5

# Task 1
# Create playlist_ids list

playlist_ids = [101, 102, 103, 104, 105]

print(playlist_ids)

# Output:
# [101, 102, 103, 104, 105]


# Task 2
# Add items using append() and extend()

playlist_ids.append(106)
playlist_ids.extend([107, 108])

print(playlist_ids)

# Output:
# [101, 102, 103, 104, 105, 106, 107, 108]


# Task 3
# Remove last played song using pop()

removed_song = playlist_ids.pop()

print("Removed Song ID:", removed_song)
print("Updated Playlist:", playlist_ids)

# Output:
# Removed Song ID: 108
# Updated Playlist: [101, 102, 103, 104, 105, 106, 107]


# Task 4
# Tuple immutability example

insta_filters = ("Normal", "Clarendon", "Juno", "Lark")

#insta_filters[0] = "Vintage"
print(insta_filters)

# Output:
# TypeError: 'tuple' object does not support item assignment


# Task 5
# List vs Tuple explanation

# Zomato orders -> List (because it changes daily)
# IPL teams -> Tuple (because teams are fixed and do not change)

print("Zomato orders → List (mutable, can change)")
print("IPL teams → Tuple (immutable, fixed data)")

# Output:
# Zomato orders → List (mutable, can change)
# IPL teams → Tuple (immutable, fixed data)