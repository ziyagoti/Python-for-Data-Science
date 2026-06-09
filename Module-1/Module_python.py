# Data Science Assignments - Module 1 (Python)

#Name: Ziya Goti
#Subject: Data Science

#1.Write a python program to sum of the first n positive integers.

n = int(input("Enter n: "))

s = 0
for i in range(1, n + 1):
    s += i

print("Sum =", s)

#Output:
#Enter n: 5
#Sum = 15


#2.Write a Python program to count occurrences of a substring in a string.

string = input("Enter string: ")
sub = input("Enter substring: ")

count = string.count(sub)

print("Occurrences:", count)

#Output:
#Enter string: banana
#Enter substring: na
#Occurrences: 2


# 3. Write a Python program to count the occurrences of each word in a given sentence.

sentence = input("Enter sentence: ")

words = sentence.split()

d = {}

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)

# Output:
# Enter sentence: hello hi hello bye hi hello ziya
# {'hello': 3, 'hi': 2, 'bye': 1, 'ziya': 1}

# 4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

print(new_str1 + " " + new_str2)

# Output:
#Enter first string: ziya
#Enter second string: goti
#goya ziti

# 5. Write a Python program to add 'ing' at the end of a given string.

string = input("Enter string: ")

if len(string) < 3:
    print(string)
elif string.endswith("ing"):
    print(string + "ly")
else:
    print(string + "ing")

# Output:
# Enter string: play
# playing

# 6. Write a Python program to replace 'not...poor' with 'good'.

s = input("Enter string: ")

not_pos = s.find("not")
poor_pos = s.find("poor")

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
    s = s[:not_pos] + "good" + s[poor_pos + 4:]

print(s)

# Output:
# Enter string: The movie is not that poor
# The movie is good

# 7. Program to find Greatest Common Divisor of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)

# Output:

# Enter first number: 20
# Enter second number: 28
# GCD = 4

# 8. Write a Python program to check whether a list contains a sublist.

main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]

found = False

for i in range(len(main_list) - len(sub_list) + 1):
    if main_list[i:i+len(sub_list)] == sub_list:
        found = True

print(found)

# Output:
# True

# 9. Write a Python program to find the second smallest number in a list.

lst = [5, 2, 8, 1, 3]

lst = list(set(lst))
lst.sort()

print("Second Smallest =", lst[1])

# Output:
# Second Smallest = 2

# 10. Write a Python program to get unique values from a list.

lst = [1, 2, 2, 3, 4, 4, 5]

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)
# Output:
# [1, 2, 3, 4, 5]

# 11. Write a Python program to unzip a list of tuples into individual lists.

lst = [(1, 2), (3, 4), (5, 6)]

a, b = zip(*lst)

print(list(a))
print(list(b))

# Output:
# [1, 3, 5]
# [2, 4, 6]

# 12. Write a Python program to convert a list of tuples into a dictionary.

lst = [("a", 1), ("b", 2), ("c", 3)]

d = dict(lst)
print(d)

# Output:
# {'a': 1, 'b': 2, 'c': 3}

# 13. Write a Python program to sort a dictionary (ascending/descending) by value.

d = {'a': 5, 'b': 2, 'c': 8}

asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print("Ascending:", asc)
print("Descending:", desc)

# Output:

# Ascending: {'b': 2, 'a': 5, 'c': 8}
# Descending: {'c': 8, 'a': 5, 'b': 2}

# 14. Write a Python program to find the highest 3 values in a dictionary.

d = {'a': 10,
     'b': 50,
     'c': 30,
     'd': 70,
     'e': 20
}

values = sorted(d.values(), reverse=True)
print(values[:3])

# Output:
# [70, 50, 30]

# 15. Given a number n, print Fibonacci series up to n.

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("First few Fibonacci numbers are:")

for i in range(n + 1):
    print(a, end=" ")
    a, b = b, a + b
# Output:
#Enter number of terms: 7
#First few Fibonacci numbers are:
#0 1 1 2 3 5 8 13


# 16. Counting the frequencies in a list using a dictionary.

lst = [1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]

d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for key in sorted(d):
    print(key, ":", d[key])

# Output:
# 1 : 5
# 2 : 4
# 3 : 3
# 4 : 3
# 5 : 2

# 17. Write a python program using function to find the sum of odd series and even series.

import math

def odd_series(n):
    s = 0
    for i in range(1, n + 1, 2):
        s += (i ** 2) / math.factorial(i)
    return s

def even_series(n):
    s = 0
    for i in range(2, n + 1, 2):
        s += (i ** 2) / math.factorial(i)
    return s

n = int(input("Enter n: "))

print("Odd Series Sum =", odd_series(n))
print("Even Series Sum =", even_series(n))

# Output:
# Enter n: 6
# Odd Series Sum = 2.7083333333333335
# Even Series Sum = 2.716666666

# 18. Python Program to Find Factorial of Number Using Recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

num = int(input("Enter number: "))

print("Factorial =", factorial(num))

# Output:

# Enter number: 5
# Factorial = 120

# 19. Write a Python function that takes a list and returns a new list with unique elements.

def unique_list(lst):
    unique = []

    for i in lst:
        if i not in unique:
            unique.append(i)

    return unique

lst = [1, 2, 2, 3, 4, 4, 5]

print(unique_list(lst))

# Output:

# [1, 2, 3, 4, 5]

# 20. Mini Project - Password Generator
import random

class User:

    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)

    def display(self):
        print("User Details:", self.details)

def generate_password(text):

    words = text.split()

    if len(words) < 2:
        raise ValueError("Please enter at least two words.")

    selected = random.sample(words, min(2, len(words)))

    password = ""

    for word in selected:
        password += word.capitalize()

    password += str(random.randint(100, 999))
    password += random.choice("@#$%&*!")

    if len(password) < 8:
        password += "ABC123"

    return password

try:

    user_id = int(input("Enter User ID: "))
    name = input("Enter Name: ")
    text = input("Enter some words for password generation: ")

    password = generate_password(text)

    user = User(user_id, name, password)

    print("Generated Password:", password)
    user.display()

except ValueError as e:
    print("Error:", e)

# Output:
# Enter User ID: 101
# Enter Name: ziya
# Enter some words for password generation: python for data science
# Generated Password: PythonData939*
# User Details: (101, 'ziya', 'PythonData939*')
