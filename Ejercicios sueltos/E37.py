"""

Program: E37.py
Author: Alberto Sánchez Barona
Date: 13/10/2022
Description:  Develop a program that enters by keyboard 10 numbers and, for each of them, display one of the following
              messages depending on its value:
              • Ice, if the number is equal or lower to 0.
              • Water, if the number is higher than 0 and lower than 100.
              • Vapor, if the number is higher than 100.

"""

cont = 1

while cont <= 10:
    number = float(input(f"Enter a number {cont}/10: "))
    cont += 1
    if number <= 0:
        print("Ice")
    elif number > 0 and number <= 100:
        print("Water")
    else:
        print("Vapor")
