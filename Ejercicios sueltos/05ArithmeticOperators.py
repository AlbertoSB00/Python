"""

Program: 05ArithmeticOperators.py
Author: Alberto Sánchez Barona
Date: 28/09/2022
Description: Which are the arithmetic operators and how the works.

"""

# Operator is a symbol that represents an operation. The operations are executed with operands or the date involved.
# Operators can be unary or binary. Unary operators need one unique operand. Binary operators need two operands.
# We can combine several operators and operands to form an expressions.
# --------------------------------------
# The arithmetic operators are used to express arithmetic operations.
# Addition.
# Subtraction.
# Multiplication.
# / Division (the result has float datatype)
# // Integer division (the result has integer datatype)
# % Module or the rest of the integer division.
# ** Power.
# + Unary for position numbers.
# - Unary for negative numbers.

integer_number = 5
float_number = 3.5
addition = integer_number + float_number
print("The addition is", addition)

subtraction = float_number - integer_number
print("The subtraction is", subtraction)

multiplication = float_number * integer_number
print("The multiplication is", multiplication)

division = integer_number / float_number
print("The division is", division, "and datatype is", type(division))

integer_division = integer_number // integer_number
print("The division is", integer_division, "and datatype is", type(integer_division))

# Module operator
money = 11
students = 3
module = money % students
print(f"The rest of the integer division between {money} and {students} is {module}")

# Power operator
b = 2
exponent = 3
power = b ** exponent
print(f"The power of {b} raised to {exponent} is {power}")

# Minus unary operator
negative_number = -5
my_age = +21
print(f"5 years ago I was {my_age + negative_number} old")