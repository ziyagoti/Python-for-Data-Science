#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-20


# Task 1
# Playlist class with private attribute

class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def show_playlist(self):
        print(self._songs)

p1 = Playlist()
p1.add_song("Song A")
p1.add_song("Song B")
p1.add_song("Song C")

p1.show_playlist()

# Output:
# ['Song A', 'Song B', 'Song C']


# Task 2
# Product class with getter and setter

class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = new_price

p = Product(1000)

print(p.get_price())
p.set_price(1500)
print(p.get_price())

# Output:
# 1000
# 1500


# Task 3
# Movie rating validation

class Movie:
    def __init__(self, rating):
        self._rating = rating

    def get_rating(self):
        return self._rating

    def set_rating(self, value):
        if 0 <= value <= 10:
            self._rating = value
        else:
            print("Error: Rating must be between 0 and 10")

m = Movie(8.5)

print(m.get_rating())
m.set_rating(9.2)
print(m.get_rating())
m.set_rating(15)

# Output:
# 8.5
# 9.2
# Error: Rating must be between 0 and 10


# Task 4
# Abstraction using abstract class

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Paytm(PaymentMethod):
    def pay(self, amount):
        print("Paid", amount, "using Paytm")

class PhonePe(PaymentMethod):
    def pay(self, amount):
        print("Paid", amount, "using PhonePe")

p1 = Paytm()
p2 = PhonePe()

p1.pay(500)
p2.pay(1000)

# Output:
# Paid 500 using Paytm
# Paid 1000 using PhonePe