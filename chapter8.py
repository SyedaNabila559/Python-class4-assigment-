#####   Lesson 08: Control Modules & Functions  #####

# What is a Module in Python?
# A module in Python is a file that contains Python code (functions, classes, variables, or even runnable code) and is used to organize and reuse code efficiently.

# Types of Modules in Python

# 1. Standard Library Modules (Pre-installed modules in Python)
import math
print(math.sqrt(16))  # Output: 4.0

# 2. User-Defined Modules (Custom Modules) (Any Python file (.py) you create can be used as a module.)
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Import and use it in another script
# main.py
# import my_module  # my_module.py ko import krna

# greet() use function
# print(my_module.greet("Ali"))  # Output: Hello, Ali!

# add() add new
# print(my_module.add(5, 3))  # Output: 8

# 3. External Modules (Third-party Libraries) ( calling APIS like  numpy, pandas, requests)
import requests

response = requests.get("https://api.example.com/data")
print(response.text)

# How to Import a Module in Python?

# 1. Basic Import
import math  # Importing the math module
print(math.sqrt(16))  # Output: 4.0

# 2. Importing Specific Functions or Variables
from math import sqrt  # Importing only the sqrt function from math
print(sqrt(16))  # Output: 4.0

# 3. Importing with an Alias
import numpy as np  # Importing numpy with alias np
arr = np.array([1, 2, 3, 4])
print(arr)  # Output: [1 2 3 4]

# 4. Importing All Functions/Variables (Not Recommended)
from math import *  # Importing everything from the math module
print(sqrt(16))  # Output: 4.0

##### Understanding Functions in Python #####
# Simple Function
def greet():
    print("Hello, welcome to Python!")
    
greet()  # Calling the function

# 1. Built-in Functions
print(len("Hello"))  # Output: 5

# 2. User-defined Functions
def greet(name):
    return f"Hello, {name}!" 
print(greet("Alice"))  # # Output: Hello, Alice!

# 3. Functions defined in built-in modules
import random
print(random.random())

#  Pass by Object Reference with Mutable Objects (e.g., List, Dictionary)
def modify_list(lst):
    lst.append(4)  # Modify the original list

my_list = [1, 2, 3]
modify_list(my_list)

print(my_list)  # Output: [1, 2, 3, 4]

# Pass by Object Reference with Immutable Objects (e.g., Integer, String)
def modify_number(n):
    n = n + 1  # This creates a new integer object

x = 5
modify_number(x)

print(x)  # Output: 5

# Function Arguments

# 1. Positional Arguments (When you pass values to a function, they are assigned to the corresponding parameters based on their position.)
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling the function with positional arguments
greet("Alice", 25)  # Output: Hello Alice, you are 25 years old.

# 2. Keyword Arguments (Keyword arguments allow you to pass values to a function by specifying the name of the parameter.)
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling the function with keyword arguments
greet(age=25, name="Alice")  # Output: Hello Alice, you are 25 years old.

# 3. unpacking iterables (Python allows you to use the * operator to unpack elements from an iterable into a variable, especially useful when you don’t know how many elements are in the iterable, or when you want to capture extra elements.)
# Unpacking with * in a List or Tuple
# Extended unpacking with a list
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)  # Output: 5

# 4. Variable-length Arguments (Arbitrary Arguments) (Python allows you to pass a variable number of arguments to a function using *args for non-keyword arguments and **kwargs for keyword arguments.)
# (Non-keyword Variable-Length Arguments)  ((Non-keyword Variable-Length Arguments)
# *args allows you to pass a variable number of positional arguments to a function. These arguments are collected into a tuple inside the function.
def greet(*names):
    for name in names:
        print(f"Hello {name}")

# Calling the function with different numbers of arguments
greet("Alice", "Bob", "Charlie")
# Output:
# Hello Alice
# Hello Bob
# Hello Charlie

#  (Keyword Variable-Length Arguments)
# **kwargs allows you to pass a variable number of keyword arguments to a function. These arguments are collected into a dictionary inside the function.
def greet(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
greet(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

# Python Function with Return Value
def add_numbers(a, b):
    result = a + b
    return result

# Call the function and print the returned value
sum = add_numbers(3, 5)
print(sum)  # Output: 8

#   Anonymous Functions
# Basic Lambda Function (A simple example of a lambda function that adds two numbers)
add = lambda x, y: x + y

# Call the lambda function
result = add(3, 5)
print(result)  # Output: 8

# Lambda Function in a List (You can use lambda functions within other functions or structures like map(), filter(), or sorted())
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Generator Function (Generators allow you to handle large datasets more efficiently by generating values on-the-fly, which can save memory compared to returning all values at once. They are useful for scenarios where you need to work with a sequence of data, but you don't want to load the entire sequence into memory at once.)

#  Simple Generator Function
def count_up_to_three():
    yield 1
    yield 2
    yield 3

# Using the generator
counter = count_up_to_three()

# Iterating over the generator
for number in counter:
    print(number)

# Infinite Sequence
# counter = infinite_counter()

# for num in counter:
#     if num > 5:  # Stop when the number exceeds 5
#         break
#     print(num)

# Generator Expressions
squares = (x**2 for x in range(1, 6))

# Using the generator
for square in squares:
    print(square)


########### ************************ ##################
