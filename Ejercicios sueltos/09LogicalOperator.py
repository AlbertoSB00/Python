"""

Program: 09LogicalOperator.py
Author: Alberto Sánchez Barona
Date: 30/09/2022
Description: Example about logical operators and how they work.

"""

# Logical operators always work with logical/boolean operands.
# As there is no very much booleans data literals o variables they usually get together two or more relational
# expressions (comparisons).
# How to they work? They are ruled by the true tables.
# and -> Logical disjunction (binary)
# or -> Logical conjunction (binary)
# not -> Logical negation (unary)

# and operator
# The true table of and operator
# Operand1      Operand2        Op1 and Op2
# -----------------------------------------
# True          True            True
# True          False           False
# False         True            False
# False         False           False
print("--------------------------------------------------------------------")
min_age = 18
min_height = 1.75
your_age = int(input("Enter your age: "))
your_height = float(input("Enter your height: "))
print("--------------------------------------------------------------------")
result = your_age >= min_age and your_height > min_height
print("1.- The result is:", result)
print("1.- The datatype of logical operator and: ", type(result))
print("--------------------------------------------------------------------")

# op operator
# The true table of and operator
# Operand1      Operand2        Op1 or Op2
# -----------------------------------------
# True          True            True
# True          False           True
# False         True            True
# False         False           False
result = your_age >= min_age or your_height > min_height
print("2.- The result is:", result)
print("2.- The datatype of logical operator and: ", type(result))
print("--------------------------------------------------------------------")

# not operator
# The true table of not operator
# Operand1      not Operand
# --------------------------
# True          False
# False         True
password = "abcd1234@"
pass_user = input("3.- Enter the password: ")
result = not pass_user == password
print("3.- Is your wrong password?", result)
print("--------------------------------------------------------------------")

# More examples
result = your_age < 18 and your_height < 1.68
print("4.- Can you enter in the aquatic attractions?", result)
print("--------------------------------------------------------------------")

result = your_age >= 18 and pass_user != password
print("5.- Is your password wrong and your age is too old?", result)
print("--------------------------------------------------------------------")

result = not your_age < 18
print("6.- Are you an adult?", result)
print("--------------------------------------------------------------------")

result = not your_age > 18
print("7.- Are you an underage?", result)
print("--------------------------------------------------------------------")
