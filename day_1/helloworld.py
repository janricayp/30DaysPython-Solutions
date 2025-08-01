import math

print(3 + 4)  # Addition
print(3 - 4)  # Subtraction
print(3 * 4)  # Multiplication
print(3 / 4)  # Division
print(3 % 4)  # Modulus
print(3 ** 4)  # Exponentiation
print(3 // 4)  # Floor Division

print("Jan")  # String Your Name
print("Ybanez")  # String Your Surname
print("Philippines")  # String Your Country
# String I am enjoying 30 Days of Python
print("I am enjoying 30 Days of Python")

int_number = 3  # Integer type
float_number = 3.14  # Float type
complex_number = 3 + 4j  # Complex type
boolean_type = True  # Boolean type
list_type = [1, 2, 3, 4, 5]  # List type
tuple_type = (1, 2, 3, 4, 5)  # Tuple type
set_type = {1, 2, 3, 4, 5}  # Set type
dictionary_type = {"name": "Jan", "age": 30,
                   "country": "Philippines"}  # Dictionary type
string_type = "I am enjoying 30 Days of Python"  # String type

print(int_number)  # printing the integer type
print(float_number)  # printing the float type
print(complex_number)  # printing the complex type
print(string_type)  # printing the string type
print(boolean_type)  # printing the boolean type
print(list_type)  # printing the list type
print(tuple_type)  # printing the tuple type
print(set_type)  # printing the set type
print(dictionary_type)  # printing the dictionary type

x1 = 2  # x1 coordinate
y1 = 3  # y1 coordinate
x2 = 10  # x2 coordinate
y2 = 8  # y2 coordinate
# Euclidean distance formula
euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(round(euclidean_distance, 2))  # printing the rounded Euclidean distance
