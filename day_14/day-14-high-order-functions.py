# Day 14 : High Order Functions
# Exercises: Level 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(function, iterable)
# applies to function to each element
string_num = list(map(str, numbers))
print(string_num)

# using lambda function
string_num = list(map(lambda x: str(x), numbers))
print(string_num)

# filter(function, iterable)
# takes a function that returns True or False / only keeps elements for which returns True
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False
even_number = list(filter(is_odd, numbers))
print(even_number)

# reduce(function, iterable)
# function must take two args and reduce repeatedly
from functools import reduce

def sum(x, y):
    return int(x) + int(y)
total = reduce(sum, numbers)
print(total)

# High Order Functions are functions that takes function as parameter or return a function
# A Decorator is a design pattern in python that allows a user to add new functionality to an existing object
# A Closure allows an inside function to access the outer scope 

def print_item(item):
    print(item)

list(map(print_item, countries))

# Print countries
for country in countries:
    print(country)

# Print names
for name in names:
    print(name)

# Print numbers
for num in numbers:
    print(num)

# Exercises: Level 2
# 1
def uppercase(para):
    return para.upper()

countries_upper = list(map(lambda country: uppercase(country), countries))
print(countries_upper)

# 2
square = list(map(lambda x: x ** 2, numbers))
print(square)

# 3
names_upper = list(map(lambda name: name.upper(), names))
print(names_upper)

# 4
land_countries = list(filter(lambda country: 'land' in country, countries))
print(land_countries)

# 5
country_6_letters = list(filter(lambda country: len(country) == 6, countries))
print(country_6_letters)

# 6
country_more_letters = list(filter(lambda country: len(country) >= 6, countries))
print(country_more_letters)

# 7
e_countries = list(filter(lambda country: country[0] == 'E', countries))
print(e_countries)

# 8
squared = map(lambda x: x ** 2, numbers)
even_squares = filter(lambda x: x % 2 == 0, squared)
result = reduce(lambda x, y: x + y, even_squares, 0)
print(result)

# 9
def get_string_lists(lst):
    strings = [str for str in lst if type(str) == "str"]
    return strings
strs = list(filter(get_string_lists, names))
print(strs)