"""

Program: E24.py
Author: Alberto Sánchez Barona
Date: 17/10/2022
Description: Develop a program that gets the quotient and the rest of two positive integers via successive subtractions.

"""

number1 = int(input("Enter a first positive number: "))
number2 = int(input("Enter a second positive number: "))

accumulator = number1
quotient = 0

while True:
    print(f"{accumulator} {number2} {quotient}")
    accumulator -= number2
    quotient += 1
    if accumulator <= 0:
        break