#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-15

# Task 1
# Song duration per minute with exception handling

def get_song_duration_per_minute(total_duration, songs):
    try:
        result = total_duration / songs
        print("Duration per song:", result)
    except ZeroDivisionError:
        print("Error: Number of songs cannot be zero")
    finally:
        print("Calculation completed")

get_song_duration_per_minute(120, 0)

# Output:
# Error: Number of songs cannot be zero
# Calculation completed


# Task 2
# Flipkart price per item calculator

try:
    total_amount = int(input("Enter cart amount: "))
    items = int(input("Enter item count: "))

    price_per_item = total_amount / items
    print("Price per item:", price_per_item)

except ZeroDivisionError:
    print("Error: Item count cannot be zero")

# Output:
#Enter cart amount: 1000
#Enter item count: 0
#Error: Item count cannot be zero

# Task 3
# Custom exception for Paytm cashback

class NoOffersApplied(Exception):
    pass

try:
    spend = int(input("Enter total spend: "))
    offers = int(input("Enter number of offers: "))

    if offers == 0:
        raise NoOffersApplied("No offers applied")

    cashback = spend / offers
    print("Average cashback per offer:", cashback)

except NoOffersApplied as e:
    print("Error:", e)

# Output:
#Enter total spend: 1000
#Enter number of offers: 1
#Average cashback per offer: 1000.0


# Task 4
# Fix buggy code with exception handling

def calculate_average_rating(total_rating, num_reviews):
    try:
        return total_rating / num_reviews
    except ZeroDivisionError:
        return "Invalid input: reviews cannot be zero"
    finally:
        print("Thank you for using the calculator")

print(calculate_average_rating(500, 0))

# Output:
# Thank you for using the calculator
# Invalid input: reviews cannot be zero


# Task 5
# Safe Zomato bill split

def safe_divide_for_zomato(bill, people):
    try:
        result = bill / people
    except ZeroDivisionError:
        print("Error: Cannot divide bill by zero people")
    else:
        print("Each person pays:", result)
    finally:
        print("Split calculation done")

safe_divide_for_zomato(1200, 4)

# Output:
# Each person pays: 300.0
# Split calculation done