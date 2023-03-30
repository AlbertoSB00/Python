"""

Program: 08StringOperators.py
Author: Alberto Sánchez Barona
Date: 29/09/2022
Description: Example of use of string operator.

"""

# Operator = -> Concatenation. To concatenate strings.
# Operator in -> To look for substring in a string.

# We can concatenate string with the + operator even if they are string, literals and variables.
name = "Alberto"
last_name = "Sánchez"
surname = "Barona"

full_name = name + " " + last_name + " " + surname
print("The full name is:", full_name)

full_name = "Peter " "Parker " "Spider-man"
print("The full name is:", full_name)

# The previous characteristic is very useful to form a very long string in several lines.
full_name = "Carlos Alberto Gustavo Felipe Maximiliano de Battemberg y Baja Sajonia emperador del Sacro Imperio Romano"
print("The full name is:", full_name)

# In operator
name = "John"
full_name = "David John Smith"
result = name in full_name
print("Is John inside the full name?", result)

name = "john"
full_name = "David John Smith"
result = name in full_name
print("Is John inside the full name?", result)