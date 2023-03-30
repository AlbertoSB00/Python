"""

Program: E34.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description:  Develop a program that enters by keyboard numbers until one which has an integer square root.

"""

number = float(input("Enter a number: "))
square_root = number ** 0.5
print("The result is", square_root)
while int(square_root) != square_root:
    number = float(input("Enter a number: "))
    square_root = number ** 0.5
    print("The result is", square_root)