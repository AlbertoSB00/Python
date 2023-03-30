"""

Program: 04InputOutput.py
Author: Alberto Sánchez Barona
Date: 28/09/2022
Description: How to do the input by keyboard and the output on the screen. Functions input() and print()

"""

my_age = input("Enter your age: ")
print("Your age is", my_age)
print(type(my_age))

# We must control what user enters by keyboard.
my_age = int(input("What is your age? "))
print("The entered age is", my_age)

# All date entered by user input() function are string datatype.
print(type(my_age))
in_10_years = my_age + 10
print("In 10 years you are", in_10_years, "old")

# The float() function to convert from str to float.
my_weight = float(input("Enter your weight: "))
print("Your weight is", my_weight)

# The print() function to the output on the screen.
print("My age is", my_age, "and my weight is", my_weight)

# We can change the last character use to print()
print("My age is", end="-")
print(my_age, end="-")
print("My weight is", end="-")
print(my_weight)

separator_character = "@"
user = "pepito"
domain = "hotmail.com"
print("Email", end=" ")
print(user, end=separator_character)
print(domain)

# Formatted strings in python are called f strings. An f strings are literal string with a prefix. The prefix is
# f or F. In an f string we can include expressions to be showed.
min_age = 10
max_age = 65
your_age = int(input(f"Enter your age between {min_age} and {max_age}: "))
print(f"Your age is {your_age}")

# Even we can show float date with some precision.
pi = 3.14159921413
print(f"The number pi is {pi}")
print(f"The number pi is {pi:{10}.{6}f}")