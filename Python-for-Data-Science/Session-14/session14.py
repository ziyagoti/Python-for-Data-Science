#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-14

# Task 1
# Write songs into playlist.txt

file = open("playlist.txt", "w")

file.write("Song A\n")
file.write("Song B\n")
file.write("Song C\n")
file.write("Song D\n")
file.write("Song E\n")

file.close()

# Output:
# playlist.txt file created with 5 songs


# Task 2
# Read file and print in uppercase

file = open("playlist.txt", "r")

for song in file:
    print(song.strip().upper())

file.close()

# Output:
# SONG A
# SONG B
# SONG C
# SONG D
# SONG E


# Task 3
# Read CSV and print winners

import csv

file = open("ipl.csv", "r")
reader = csv.reader(file)
next(reader)

for row in reader:
    print(row[3])

file.close()

# Output:
# CSK
# MI
# SRH

# Task 4
# Load JSON and print title + rating

import json

file = open("movies.json", "r")

movies = json.load(file)

for movie in movies:
    print(movie["title"], movie["rating"])

file.close()

# Output:
# Pathaan 8.2
# Jawan 8.5
# Animal 7.9


# Task 5
# Check file using pathlib and create JSON if not exists

from pathlib import Path
import json

path = Path("my_fav_apps.json")

if not path.exists():
    data = [
        {"name": "Instagram", "category": "Social"},
        {"name": "Zomato", "category": "Food"},
        {"name": "Paytm", "category": "Finance"}
    ]

    file = open("my_fav_apps.json", "w")
    json.dump(data, file)
    file.close()
    print("my_fav_apps.json created with 3 apps")
else:
    print("File already exists")
# Output:
# File already exists