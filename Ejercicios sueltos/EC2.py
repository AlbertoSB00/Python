"""

Program: EC2.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description: Develop a program that enters by keyboard two numbers and display on the screen the division. Be careful!
             if the division if 0 the program must display and error.

"""

number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

if number1 == 0 or number2 == 0:
    print("ERROR -> Don't introduce 0")
if number1 != 0 or number2 != 0:
    result = number1 / number2
    print("The result is", result)