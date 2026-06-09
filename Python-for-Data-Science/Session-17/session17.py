#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-17


# Task 1
# math module sqrt

import math

value = 225
sqrt_result = math.sqrt(value)

print("Square root:", sqrt_result)

# Output:
# Square root: 15.0


# Task 2
# os module folder create

import os

folder = "MyDownloads"

os.makedirs(folder, exist_ok=True)

full_path = os.path.abspath(folder)

print("Folder created at:", full_path)

# Output:
#Folder created at: C:\Users\Admin\PycharmProjects\Python-for-Data-Science\Session-17\MyDownloads


# Task 3
# datetime formatting

from datetime import datetime

now_time = datetime.now()

time_format = now_time.strftime("%d-%m-%Y %H:%M:%S")

print("Current Time:", time_format)

# Output:
#Current Time: 09-06-2026 15:17:51


# Task 4
# custom module: playlist_utils.py

import playlist_utils
playlist = []

playlist = playlist_utils.add_song(playlist, "Song A")
playlist = playlist_utils.add_song(playlist, "Song B")
playlist = playlist_utils.add_song(playlist, "Song C")

print("Final Playlist:", playlist)

# Output:
# Final Playlist: ['Song A', 'Song B', 'Song C']


# Task 5
# requests version check
#pip install requests
import requests

print("Requests Version:", requests.__version__)

# Output:
#Requests Version: 2.34.2
