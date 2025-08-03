# Day 6 - Tuples

# Exercise: Level 1

bro = ('luffy', 'ace', 'sabo')
sis = ('hancock', 'yamato', 'koala')
siblings = bro + sis
print(len(siblings))
one_piece = list(siblings)
one_piece.append('dragon')
one_piece.append('crocodile')
print(one_piece)

# Exercise: Level 2
siblings = one_piece[:6]
parents = one_piece[-2:]
print(siblings)
print(parents)

fruits = ('apple', 'strawberry', 'peach')
vegetables = ('eggplant', 'ampalaya', 'sayote')
animal_products = ('pork', 'steak', 'adobo')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[3:5])
print(food_stuff_lt[:3])
del food_stuff_tp
# print(food_stuff_tp) -- task: check if an item exist

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
