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

