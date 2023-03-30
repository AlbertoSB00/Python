"""

Program:        22FunctionsVI.py
Author:         Alberto Sánchez Barona
Date:           28/10/2022
Description:    Example of recursive.

Develop a function to calculate the factorial of a integer number

"""


def factorial(number):
    if number == 1:
        result = 1
    else:
        result = number * factorial(number - 1)
    return result


number = int(input("Enter the number: "))
f = factorial(number)
print(f"The factorial of {number} is {f}")