fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"Your index is not in the range of 0 {len(fruits)-1}")
    else:
        print(fruit + " pie")
    

make_pie(4)

fb_posts = [
    {"Likes": 21, "comments": 2},
    {"Likes": 13, "comments": 2, "shares": 1},
    {"Likes": 31, "comments": 8, "shares": 3},
    {"comments": 4, "shares": 2},
    {"comments": 1, "shares": 1},
    {"Likes": 19, "comments": 3}
]

total_likes = 0

for post in fb_posts:
    try:
        post["Likes"]
    except KeyError:
        print("Key (likes) not in dcitionary ")
    else:
        total_likes = total_likes + post["Likes"]

print(total_likes)