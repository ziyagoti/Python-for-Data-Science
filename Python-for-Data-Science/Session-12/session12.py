#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-12

# Task 1
# Convert song titles to lowercase using map + lambda

songs = ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita']

to_lower = lambda x: x.lower()

clean_songs = list(map(to_lower, songs))

print(clean_songs)

# Output:
# ['shape of you', 'blinding lights', 'levitating', 'senorita']


# Task 2
# Filter ratings above 4.0

ratings = [4.2, 3.8, 4.5, 2.9, 3.5]

high_ratings = list(filter(lambda x: x > 4.0, ratings))

print(high_ratings)

# Output:
# [4.2, 4.5]


# Task 3
# Reduce to calculate total cart price

from functools import reduce

cart = [499, 1299, 299, 799]

total = reduce(lambda x, y: x + y, cart)

print(total)

# Output:
# 2896


# Task 4
# Format followers (K / M) using map

def format_followers(num):
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    else:
        return str(num)

counts = [950, 1500, 25000, 1200000]
result = list(map(format_followers, counts))
print(result)

# Output:
# ['950', '1.5K', '25.0K', '1.2M']


# Task 5
# Filter odd numbers using lambda

scores = [101, 98, 120, 77, 88]

even_scores = list(filter(lambda x: x % 2 == 0, scores))

print(even_scores)

# Output:
# [98, 120, 88]