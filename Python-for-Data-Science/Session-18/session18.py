#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-18


# Task 1
# Extract phone numbers using re.findall()

import re

text1 = "Call me at +91-9876543210 or +91-9123456789"

phones = re.findall(r"\+91-\d{10}", text1)

print("Phone Numbers:", phones)

# Output:
# Phone Numbers: ['+91-9876543210', '+91-9123456789']


# Task 2
# Check valid date using re.search()

def check_date(text):
    match = re.search(r"\b\d{2}/\d{2}/\d{4}\b", text)
    return bool(match)

print(check_date("My birthday is 12/08/2024"))

# Output:
# True


# Task 3
# Extract prices and sum them

text2 = "Items: Rs. 299, Rs. 1500, Rs. 450"

prices = re.findall(r"Rs\. (\d+)", text2)

total = sum(int(p) for p in prices)

print("Total Price:", total)

# Output:
# Total Price: 2249


# Task 4
# Replace emails using re.sub()

text3 = "Contact: abc@gmail.com and xyz@yahoo.com"

hidden = re.sub(r"\S+@\S+", "[hidden email]", text3)

print(hidden)

# Output:
# Contact: [hidden email] and [hidden email]


# Task 5
# Extract Instagram usernames

text4 = """
@ziya_01 nice post
@user123 awesome
@ab good
@insta_user test
@hello_world amazing
"""

users = re.findall(r"@[A-Za-z0-9_]{3,}", text4)

unique_users = list(set(users))

print("Usernames:", unique_users)

# Output:
#Usernames: ['@user123', '@hello_world', '@ziya_01', '@insta_user']
