# ExerciseS: level 1
# 1
import math 

def add_two_numbers(x, y):
    sum = x + y
    return sum
print(add_two_numbers(3, 8))

# 2
def area_of_circle(r):
    area = math.pi * r * r
    return area
print(f"{area_of_circle(10):.2f}")

# 3
def add_all_nums(*args):
    # Check if all args are numbers (int or float)
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "Error: All arguments must be numbers (int or float)."
print(add_all_nums(3, 4, 7, 'y'))

# 4
def convert_celsius_to_fahrenheit(c):
    fahren = (c * 9/5) + 32
    return f"{fahren:.1f} Fahrenheit"
print(convert_celsius_to_fahrenheit(37.9))

# 5
def check_season(month):
    seasons = {
        'autumn': ['september', 'october', 'november'],
        'winter': ['december', 'january', 'february'],
        'spring': ['march', 'april', 'may'],
        'summer': ['june', 'july', 'august']
    }

    for season, months in seasons.items():
        if month.lower() in months:
            return season.capitalize()
    return "Invalid month"
print(check_season('January'))

# 6
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1) # formula for slope
    return slope
print(calculate_slope(2,4,1,7))

# 7
import cmath
def solve_quadratic_eqn(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminant) / (2*a)
    x2 = (-b - discriminant) / (2*a)
    return x1.real, x2.real                  # want real numbers not the complex
print(solve_quadratic_eqn(1, -3, 2))

# 8
def print_list(lst):
    for item in lst:
        print(item)
print_list([3, 5, 3, 4, 2])

# 9
def reverse_list(lst):
    reverse_list = []
    for i in range(len(lst) -1, -1, -1):  # start sa last index, then end, then backward
        reverse_list.append(lst[i])
    return reverse_list
print(reverse_list([3, 5, 3, 4, 2]))

# 10 
def capitalize_list_items(lst):
    capitalized = []
    for i in lst:
        capitalized.append(i.capitalize())
    return capitalized
print(capitalize_list_items(['hello', 'one piece']))

#11
def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))     

# 12
def remove_item(lst, item):
    lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# 13
def sum_of_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


#  Exercises: Level 2
# 1
def evens_and_odds(num):
    if num < 0:
        return "Please enter a positive integer."
    
    evens = 0
    odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return {"evens": evens, "odds": odds}

print(evens_and_odds(100))

# 2
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f
print(factorial(5))

# 3
def is_empty(para=None):
    if para == None or para == "":
        return "Empty"
    else:
        return para
print(is_empty(5))

# 4
import statistics

def describe_data(data):
    result = {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "mode": statistics.mode(data),
        "range": max(data) - min(data),
        "variance": statistics.variance(data),
        "std_dev": statistics.stdev(data)
    }

    for key, value in result.items():
        print(f"{key}: {value}")

data = [4, 2, 5, 8, 6, 8]
describe_data(data)

# Exercises: Level 3
# 1
def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(num ** 0.5) + 1):  # only check up to square root of num
        if num % i == 0:
            return False
    return True
print(is_prime(5))

# 2
def check_uniq(items):
    return len(items) == len(set(items))
print(check_uniq([2,3,4,4,8,9]))

# 3
def all_same_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)
print(all_same_type([1, 2, 3]))      

# 4
def is_valid_variable_name(name):
    return name.isidentifier()
print(is_valid_variable_name('name'))







 




