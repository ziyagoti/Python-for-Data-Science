#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-4

# Task 1
# Convert string to lowercase, replace dash with space

text = 'Flipkart-Sale2024'

result = text.lower().replace('-', ' ')

print(result)

# Output:
# flipkart sale2024


# Task 2
# Clean product name using strip, upper, replace

product = ' OnePlus Nord-CE 3 '

result = product.strip().upper().replace('-', ':')

print(result)

# Output:
# ONEPLUS NORD:CE 3


# Task 3
# Split product code into list

def split_product_code(product_code):
    return product_code.split('-')

code = 'ZOMATO-FOOD-2024'

print(split_product_code(code))

# Output:
# ['ZOMATO', 'FOOD', '2024']


# Task 4
# Extract "Premium" using slicing

text = 'Spotify_Premium_Offer'

result = text[8:15]

print(result)

# Output:
# Premium


# Task 5
# String formatting

product = 'Myntra Shirt'
price = 799.5
msg=f"Deal: {product} is available at ₹{price:.2f} only!"
print(msg)

# Output:
# Deal: Myntra Shirt is available at ₹799.50 only!
