age = 20 # age as an integer
weight = 47.0 # weight as float
complex_number = 3j # complex number
base = int(input("Enter base: ")) # prompt user to enter the base of a triangle
height = int(input("Enter height: ")) # height of a triange
triangle_area = 0.5 * base * height # area of a triangle
print(f"The area of the triangle is {int(triangle_area)}")

a = int(input("Enter side a: ")) # side a of a triangle in integer
b = int(input("Enter side b: ")) # side b 
c = int(input("Enter side c: ")) # side c
triangle_perimeter = a + b + c
print(f"The perimeter of the triangle is {triangle_perimeter}")

length = int(input("Enter length: "))
width = int(input("Enter width: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print(f"The area of the rectangle is {rectangle_area}")
print(f"The perimeter of the rectangle is {rectangle_perimeter}")

radius = int(input("Enter radius: "))
circle_area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius
print(f"The area of the circle is {int(circle_area)}")
print(f"The circumference of the circle is {round(circumference, 2)}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2

# Finding the x-intercept by setting y = 0
x_intercept = y_intercept * -1 / slope


# Print results
print(f"Slope: {slope}")
print(f"y-intercept: (0, {y_intercept})")
print(f"x-intercept: ({x_intercept}, 0)")



import math # importing math for the sqrt

x1, y1, x2, y2 = 2, 2, 6, 10
slope2 = (y2 - y1) / (x2 - x1)
euclidean = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

# Compare the slopes
print(f"slope 1: {slope} and slope 2: {slope2}")

for i in range(-10, 10):
    y_value = (i ** 2) + (6 * i) + 9
    if(y_value == 0):
        print(i)

# Find the length of python and dragon and make a falsy comparison statement
print(bool(len("python") < len("dragon")))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
found = 'on' in 'python' and 'on' in 'dragon'
print(found)

# Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
is_jargon = 'jargon' in sentence
print(is_jargon)

# There is no 'on' in both dragon and python
not_found = 'on' not in 'python' and 'on' not in 'dragon'
print(not_found)

# Find the length of the text python and convert the value to float and convert it to string
python_len = len('python')
as_float = float(python_len)
as_string = str(python_len)

# How do you check if a number is even or not using python?
is_even = int(input("Enter a number: ")) % 2 == 0

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
is_equal = (7 // 3) == int(2.7)
print(is_equal)

# Check if type of '10' is equal to type of 10
is_equal2 = type('10') == type(10)
print(is_equal2)

# Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(float("Enter hours: "))
rate_per_hour = int(float("Enter rate per hour: "))
pay = hours * rate_per_hour
print(f"Your weekly earning is {pay}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds_lived = 60 * 60 * 24 * 365 * years
print(f"You have lived for {seconds_lived} seconds.")

# Write a Python script that displays the following table
for i in range(1, 6):
    print(i, 1, i, i ** 2, i ** 3)
