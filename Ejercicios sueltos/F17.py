"""

Program:        F17.py
Author:         Alberto Sánchez Barona
Date:           25/10/2022
Description:    Develop a function that receives two parameters as the sides of a right-angled triangle and returns the
                hypotenuse.

"""


def hypotenuse(first_side, second_side):
    result = ((first_side ** 2) + (second_side ** 2)) ** 0.5
    return result


first_side = float(input("Enter the first side of a right-angled: "))
second_side = float(input("Enter the second side of a right-angled: "))
result = hypotenuse(first_side, second_side)
print(f"The hypotenuse of a right-angled triangle with a = {first_side} and b = {second_side} is c = {result}")