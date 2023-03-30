"""

Program: 12MatchStatement.py
Author: Alberto Sánchez Barona
Date: 05/10/2022
Description: Example of use of match statement.



# Match statement. Multi conditional branch
# It takes an expression with any datatype and compares it with patterns looking for a match. The patterns are in case
# blocks. Each case block has got:
#   A pattern to compare with the value of the expression in match statement.
#   A set of statement to execute if the pattern matches with the value of the expression.
# The first pattern that matches with the value of the expression is executed. The others are passed by.
# We can also add a default pattern just in case no pattern matches with the value of the expression.

# Syntax
# match <expression>:
#   case <pattern1>:
#       <statement1>
#       <statement2>
#       ...
#   case <pattern2>:
#       <statement1>
#       <statement2>
#       ...
#   ...
#   case _:
#       <statement1 by default>
#       <statement2 by default>
#       ...

# In its simplest way, every pattern is a literal value.
# Example
mark = int(input("Enter a mark: "))
match mark:
    case 1 | 2 | 3 | 4:
        print("You're failed.")
    case 5:
        print("Your grade is C")
    case 6:
        print("Your grade is B-")
    case 7 | 8:
        print("Your grade is B")
    case 9 | 10:
        print("Your grade is A")
    case _:
        print("Your mark is wrong.")
print("Your mark is", mark)


"""

# Another example with weekdays.
weekday = int(input("Enter a number of week day: "))
match weekday:
    case 1:
        print("You have chosen Monday.")
    case 2:
        print("You have chosen Tuesday.")
    case 3:
        print("You have chosen Wednesday.")
    case 4:
        print("You have chosen Thursday.")
    case 5:
        print("You have chosen Friday.")
    case 6 | 7:
        print("You have chosen weekend.")
    case _:
        print("The week day is out of range.")