"""

Program: 10Expressions.py
Author: Alberto Sánchez Barona
Date: 30/09/2022
Description: Use of expressions in Python.

"""

# An expression is a combination of operates and they operands that produces a result. The datatype of the expressions
# is the one of the results.
age = 20
name = "Robert"
surname = "Jones"
# Expression that combines arithmetic, relational and logical operators.
result = age + 5 / 2 >= 10 or name == "Robert" and surname != "Smith"
print("--------------------------------------------------------------------")
print("1.- The result is:", result)
print("--------------------------------------------------------------------")
# An example with operators with the same datatype (or compatibles)
age = 25
weight = 80.5
temperature = 36.7
# Arithmetic expressions. There's only arithmetic operators. So, operands can be only int or float. The datatype of
# the expression is that with higher range
result = age + 10 / 2 - weight / 3 * temperature + weight ** 2
print("2.- The result of the expression is:", result)
print("2.- The datatype is: ", type(result))
print("--------------------------------------------------------------------")
# The simplest expression is a literal value or a variable
age = 35
# In an expression there's an order of executing the operations. That is, same operators have precedence (more priority)
# to execute than others. The orders of execution are ruled by the precedence and associativity rules.
# Precedence -> Order of executions of operators.
# Associativity -> Order of executions of operators alike or with the same precedence.
# Order of preference: **              > >= < <= == !=         not
#                      -+                                      and
#                      * / // %                                or
#                      +-

result = age > 15 and temperature >= 30 or not weight > 120.5
print("3.- The result is:", result)
print("--------------------------------------------------------------------")


# Another example.
number = 8
result = number / 2 + number - 3 * 2 // 2 ** 2
print("4.- The result is:", result)
print("--------------------------------------------------------------------")

# The ** operator has got associativity by right
result = number ** 2 ** 3
print("5.- The result is:", result)
print("--------------------------------------------------------------------")

# Relational operators don't have associativity they all have the same precedent.
# result = number < 20 > 30 >= 50 -> Not possible

# Expression with different types of operators.
# Precedence:
# 1st -> Arithmetical operators. Relational operators. Logical operators.
result = number > 3 + number / 2 or number ** number - 2 <= number * 2 and not number < 8
print("6.- The result is:", result)
print("--------------------------------------------------------------------")

# We can modify the precedence and associativity by using brackets.
number = 4
result = number + 2 ** 3
print("7.- The result is:", result)
result = (number + 2) ** 3
print("7.- The result is:", result)
print("--------------------------------------------------------------------")

# Another longer example.
n1 = 3
n2 = 5
result = n1 - 4 * n2 + 3 / 4 * n1 + 3 - n1 ** 2
print("8.- The result is:", result)
result = n1 - 4 * (n2 + 3) / 4 * n1 + 3 - n1 ** 2
print("8.- The result is:", result)
result = n1 - 4 * (n2 + 3) / 4 * (n1 + 3) - n1 ** 2
print("8.- The result is:", result)
result = (n1 - 4) * (n2 + 3) / 4 * (n1 + 3) - n1 ** 2
print("8.- The result is:", result)
result = (n1 - 4) * (n2 + 3) / 4 * ((n1 + 3) - n1) ** 2
print("8.- The result is:", result)
result = ((n1 - 4) * ((n2 + 3) / (4 * ((n1 + 3) - n1)))) ** 2
print("8.- The result is:", result)
print("--------------------------------------------------------------------")

# Example to apply the brackets to change the precedence and associativity
amount = 4
price = 1000
discount = 30
total_import = (price - price * discount / 100) * amount
print("9.- The total import is:", total_import)
print("--------------------------------------------------------------------")

# We can use the brackets with logical operators.
age = 35
weight = 86.5
temperature = 36.7
result = age > 40 and weight <= 120 or temperature >= 20
print("10.- The result is", result)
result = age > 40 and (weight <= 120 or temperature >= 20)
print("10.- The result is", result)
print("--------------------------------------------------------------------")