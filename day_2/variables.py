# Day 2: 30 Days of python programming

import math
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"
country = input("Enter your country: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
year = 2025
is_married = False
is_true = True
is_light_on = True
number_1, number_2, number_3 = 5, 10, 15

print(type(first_name))  # <class 'str'>
print(type(last_name))   # <class 'str'>
print(type(full_name))   # <class 'str'>
print(type(country))     # <class 'str'>
print(type(city))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(year))        # <class 'int'>
print(type(is_married))  # <class 'bool'>
print(type(is_true))     # <class 'bool'>
print(type(is_light_on))  # <class 'bool'>
print(type(number_1))    # <class 'int'>
print(type(number_2))    # <class 'int'>
print(type(number_3))    # <class 'int'>
print(type(number_1 + number_2 + number_3))  # <class 'int'>

print(f"first name: {len(first_name)} and last name: {len(last_name)}")

num_one = 5
num_two = 4
total = num_one + num_two
print(f"Total: {total}")  # Total: 9

diff = num_one - num_two
print(f"Difference: {diff}")  # Difference: 1

product = num_one * num_two
print(f"Product: {product}")  # Product: 20

division = num_one / num_two
print(f"Division: {division}")  # Division: 1.25

remainder = num_one % num_two
print(f"Remainder: {remainder}")  # Remainder: 1

exp = num_one ** num_two
print(f"Exponent: {exp}")  # Exponent: 625

floor_division = num_one // num_two
print(f"Floor Division: {floor_division}")  # Floor Division: 1

# Area and Circumference of a Circle
radius = input("Enter the radius of the circle: ")
radius = float(radius)  # Convert input to float
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius
# Area of Circle: 2827.4333882308138
print(f"Area of Circle: {area_of_circle}")
# Circumference of Circle: 188.49555921538757
print(f"Circumference of Circle: {circum_of_circle}")
