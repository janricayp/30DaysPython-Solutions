# Day 9 - Exercise: Level 1
# 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else: 
    waiting_years = 18 - age
    year = 'year' if waiting_years == 1 else 'years'
    print(f"You need {waiting_years} more {year} to learn to drive")

# 2
own_age = 25
diff = abs(age - own_age)
if age == own_age:
    print("We are the same age")
else:
    year = 'year' if diff == 1 else 'years'
    if age > own_age:
        print(f"You are {diff} {year} older than me")
    else: 
        print(f"You are {diff} {year} younger than me")

# 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# Exercises: Level 2
# 1
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print('A')
elif 70 <= score <= 79:
    print('B')
elif 60 <= score <= 69:
    print('C')
elif 50 <= score <= 59:
    print('D')
else:
    print('F')

# 2
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

month = input("Enter a month: ").strip().title()
if month in autumn:
    print(f"{month} is autumn season")
elif month in winter:
    print(f"{month} is winter season")
elif month in spring:
    print(f"{month} is spring season")
elif month in summer:
    print(f"{month} is summer season")
else:
    print("You entered an invalid month")

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("The fruit already exist in the list.")
else:
    fruits.append(fruit)
    print(fruits)


# Exercises: Level 3
# 1

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, 
# print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - 
# for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, print the information in the following format:

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"Middle skill: {skills[middle_index]}")

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Has a Python Skill")
    else:
        print("Doesn't have Python Skill")

if 'skills' in person:
    skills = set(person['skills'])

    if skills == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print('He is a fullstack developer')
    else:
        print('Unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in {person['country']}. He is married.")