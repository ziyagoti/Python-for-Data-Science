#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-9

# Task 1
# Calculate final price after discount

def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate / 100)
    return final_price

print(calculate_final_price(1000, 10))

# Output:
# 900.0


# Task 2
# Delivery charge based on city

def get_delivery_charge(amount, city='Ahmedabad'):
    if city == 'Ahmedabad':
        return 0
    else:
        return 50

print(get_delivery_charge(500, 'Surat'))

# Output:
# 50


# Task 3
# Format price with currency

def format_price(price, currency='INR'):
    if currency == 'INR':
        return "₹" + str(price)
    else:
        return "$" + str(price)

print(format_price(500))
print(format_price(500, 'USD'))

# Output:
# ₹500
# $500


# Task 4
# Apply coupon discount

def apply_coupon(price, coupon_code=None):
    if coupon_code == 'ZOMATO10':
        return price - (price * 10 / 100)
    else:
        return price

print(apply_coupon(1000, 'ZOMATO10'))

# Output:
# 900.0