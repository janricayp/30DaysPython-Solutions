# Day 12 - Modules
# Exercises: Level 1
# 1
import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters)for i in range(6))

print(random_user_id());

# 2
def user_id_gen_by_user():
    chars = int(input())
    number_of_ids = int(input())
    characters = string.ascii_letters + string.digits
    for i in range(number_of_ids):
        user_id = ''.join(random.choice(characters) for i in range(chars))
        print(user_id)

user_id_gen_by_user()

# 3
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f"({red}, {green}, {blue})"
print(rgb_color_gen())

# Exercises: Level 2
# 1
def  list_of_hexa_colors(n=1):
    symbols = string.hexdigits.lower()[:16]
    return [f"#{''.join(random.choice(symbols)for i in range(6))}" for _ in range(n)]

print(list_of_hexa_colors())

# 2
def list_of_rgb_colors(n=1):
    return [f"rgb{rgb_color_gen()}" for _ in range(n)]
print(list_of_rgb_colors())

# 3
def generate_colors(hexa_or_rgb, number):
    mode = hexa_or_rgb.lower()
    if mode == 'hexa':
        return list_of_hexa_colors(number)
    elif mode == 'rgb':
        return list_of_rgb_colors(number)
    else:
        print("Invalid Request")
print(generate_colors('hexa', 3))

# Exercises: Level 3
# 1
def shuffle_list(lst):
    new_lst = lst[:]
    random.shuffle(new_lst)
    return new_lst
print(shuffle_list([8, 5, 6, 7, 0]))

# 2
def random_7numbers():
    random7 = random.sample(range(0, 9), 7)
    return random7
print(random_7numbers())

