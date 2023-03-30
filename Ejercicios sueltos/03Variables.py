"""

Program: 03Variables.py
Author: Alberto Sánchez Barona
Date: 26/09/2022
Description: Example of use of variables.
             What is a variable? A data with a name and value.

"""

# We create a new variable when we design a value. It must be the first operation with the variable
integer_number = 4
# Python is a deduced language, so it is found out the data type of 4 and that will be the datatype of integer_number
print(type(integer_number))


# An assignment to another variable.
my_height = 1.82
print(type(my_height))

# First, the expression after the assignment symbol is evaluated and then, the result is assigned to the variable.
radio = 5
pi = 3.14
circle = 2 * pi * radio
print("The circle has ", circle, "length")
print(type(circle))

# If we use a variable without declaring previously. It happens an error.
b = 20
height = b * 2
area_triangle = b * height / 2
print("Area of triangle is", area_triangle)

# Operations with variables.
#   Read -> Accessing to the value of variable
#   Write -> To assign a new value to a variable. We lost the previous one.
# The assignment operator is =
# We are reading the integer number variable, and we are assigning a value to the new_integer
new_integer = integer_number + 5
print("Integer number is", integer_number)
# I can keep the previous value.
old_integer_number = integer_number
integer_number = 12
print("Old value", old_integer_number, "Current value", integer_number)

# Multi assignment. We can assign several value to a several variable.
salary1, salary2, salary3 = 1000, 1200, 1500
print("Salary 1", salary1)
print("Salary 2", salary2)
print("Salary 3", salary3)

# Multi assignment. To assign the same value to several variables.
salary3 = salary2 = salary1 = 2000
print("Salary 1", salary1)
print("Salary 2", salary2)
print("Salary 3", salary3)