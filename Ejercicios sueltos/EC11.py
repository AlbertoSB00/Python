"""

Program: EC11.py
Author: Alberto Sánchez Barona
Date: 17/10/2022
Description:  Develop a program that enters numbers by keyboard until the number entered is 0. It finally displays on
              the screen the lowest number and the highest one.

"""

lowest = highest = number = int(input("Enter a number (0 to exit): "))

while number != 0:
    if lowest > number:
        lowest = number
    if highest < number:
        highest = number
    number = int(input("Enter a number (0 to exit): "))
print(f"The lowest number is {lowest} and the highest is {highest}")