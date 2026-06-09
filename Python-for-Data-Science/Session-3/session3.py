#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-3

# Task 1
# Declared variables and checked their data types using type()

age = 20
height = 165.5
name = "Ziya"
has_spotify = True

print("age", age)
print(type(age))

print("height", height)
print(type(height))

print("name", name)
print(type(name))

print("has_spotify", has_spotify)
print(type(has_spotify))

# Output:
# age 20
# <class 'int'>
# height 165.5
# <class 'float'>
# name Ziya
# <class 'str'>
# has_spotify True
# <class 'bool'>


# Task 2
# Function to calculate total cart amount

def total_cart_amount(prices):
    total = 0.0
    for price in prices:
        total = total + float(price)
    return total

cart = ['199.99', '49', '350.75']
print("Total Cart Amount:", total_cart_amount(cart))

# Output:
# Total Cart Amount: 599.74


# Task 3
# Cricket score input and condition check

score = input("Enter cricket score: ")
score = int(score)

if score >= 50:
    print("Half-century!")
else:
    print("Keep going!")

# Output (example input 60):
# Enter cricket score: 60
# Half-century!


# Task 4
# Convert string boolean to actual boolean

is_premium = "True"

if is_premium == "True":
    is_premium = True
else:
    is_premium = False

print("is_premium", is_premium)
print(type(is_premium))

# Output:
# is_premium True
# <class 'bool'>