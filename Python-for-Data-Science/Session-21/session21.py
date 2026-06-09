#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-21


# Task 1
# Product class with 10% discount

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 0.10)

p = Product("Shoes", 1000)

print(p.name, p.get_discounted_price())

# Output:
# Shoes 900.0


# Task 2
# Electronics class with 20% discount

class Electronics(Product):
    def get_discounted_price(self):
        return self.price - (self.price * 0.20)

e = Electronics("Mobile", 20000)

print(e.name, e.get_discounted_price())

# Output:
# Mobile 16000.0


# Task 3
# Polymorphism function

def show_price(item):
    print(item.name, item.get_discounted_price())

p1 = Product("Bag", 500)
e1 = Electronics("Laptop", 50000)

show_price(p1)
show_price(e1)

# Output:
# Bag 450.0
# Laptop 40000.0


# Task 4
# Ticket system

class Ticket:
    def __init__(self, movie, price):
        self.movie = movie
        self.price = price

    def get_final_price(self):
        return self.price

class PremiumTicket(Ticket):
    def get_final_price(self):
        return super().get_final_price() + 50

t1 = Ticket("Avengers", 200)
t2 = PremiumTicket("Avengers", 200)

print(t1.movie, t1.get_final_price())
print(t2.movie, t2.get_final_price())

# Output:
# Avengers 200
# Avengers 250