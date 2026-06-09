#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-19


# Task 1
# Song class basic

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

song1 = Song("Levitating", "Dua Lipa", 200)

print(song1.title)
print(song1.artist)
print(song1.duration)

# Output:
# Levitating
# Dua Lipa
# 200


# Task 2
# play preview method

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print("Playing 30-second preview of", self.title, "by", self.artist)

song2 = Song("Shape of You", "Ed Sheeran", 240)

song2.play_preview()

# Output:
# Playing 30-second preview of Shape of You by Ed Sheeran


# Task 3
# FoodOrder class with constructor

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

order1 = FoodOrder("Zomato", ["Pizza", "Coke"], 500)

print(order1.restaurant_name)
print(order1.items)
print(order1.total_price)

# Output:
# Zomato
# ['Pizza', 'Coke']
# 500


# Task 4
# add item method

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.total_price = self.total_price + item_price

order2 = FoodOrder("Swiggy", ["Burger"], 120)

order2.add_item("Fries", 80)
order2.add_item("Coke", 40)

print(order2.items)
print(order2.total_price)

# Output:
# ['Burger', 'Fries', 'Coke']
# 240


# Task 5
# default duration in Song class

class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

song3 = Song("Blinding Lights", "The Weeknd")

print(song3.title)
print(song3.duration)

# Output:
# Blinding Lights
# 0