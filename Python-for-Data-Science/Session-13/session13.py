#Name:-Ziya Goti
#Assignment:-Python for Data Science
#Session:-13

# Task 1
# Recursive function to print playlist songs

def show_songs(song_list):
    if len(song_list) == 0:
        return
    print(song_list[0])
    show_songs(song_list[1:])

my_playlist = ["Track A", "Track B", "Track C", "Track D"]

show_songs(my_playlist)

# Output:
# Track A
# Track B
# Track C
# Track D


# Task 2
# Recursive unread messages count

def total_unread(chat):
    count = chat.get('count', 0)

    for group in chat.get('subgroups', []):
        count += total_unread(group)

    return count

whatsapp_data = {
    "count": 5,
    "subgroups": [
        {"count": 3, "subgroups": []},
        {"count": 2, "subgroups": [
            {"count": 4, "subgroups": []}
        ]}
    ]
}

print(total_unread(whatsapp_data))

# Output:
# 14


# Task 3
# Scope explanation

x_value = 'global'

def outer_function():
    x_value = 'outer'

    def inner_function():
        nonlocal x_value
        x_value = 'inner'

    inner_function()
    print('Inside outer:', x_value)

outer_function()

print('Outside:', x_value)

# Output:
# Inside outer: inner
# Outside: global


# Task 4
# Recursive number format

def short_format_number(num):
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    else:
        return str(num)

print(short_format_number(1500))
print(short_format_number(1200000))
print(short_format_number(500))

# Output:
# 1.5K
# 1.2M
# 500