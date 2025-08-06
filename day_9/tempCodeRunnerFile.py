age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are old enough to drive.")
# else: 
#     waiting_years = 18 - age
#     year = 'year' if waiting_years == 1 else 'years'
#     print(f"You need {waiting_years} more {year} to learn to drive")

# # 2
# own_age = 25
# diff = abs(age - own_age)
# if age == own_age:
#     print("We are the same age")
# else:
#     year = 'year' if diff == 1 else 'years'
#     if age > own_age:
#         print(f"You are {diff} {year} older than me")
#     else: 
#         print(f"You are {diff} {year} younger than me")

# # 3
# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# if a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f"{a} is smaller than {b}")
# else:
#     print(f"{a} is equal to {b}")


# # Exercises: Level 2
# # 1
# score = int(input("Enter your score: "))
# if 80 <= score <= 100:
#     print('A')
# elif 70 <= score <= 79:
#     print('B')
# elif 60 <= score <= 69:
#     print('C')
# elif 50 <= score <= 59:
#     print('D')
# else:
#     print('F')

# # 2
# autumn = ['September', 'October', 'November']
# winter = ['December', 'January', 'February']
# spring = ['March', 'April', 'May']
# summer = ['June', 'July', 'August']

# month = input("Enter a month: ").strip().title()
# if month in autumn:
#     print(f"{month} is autumn season")
# elif month in winter:
#     print(f"{month} is winter season")
# elif month in spring:
#     print(f"{month} is spring season")
# elif month in summer:
#     print(f"{month} is summer season")
# else:
#     print("You entered an invalid month")

# # 3
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input("Enter a fruit: ").strip().lower()

# if fruit in fruits:
#     print("The fruit already exist in the list.")
# else:
#     fruits.append(fruit)
#     print(fruits)