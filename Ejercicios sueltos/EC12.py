"""

Program: EC12.py
Author: Alberto Sánchez Barona
Date: 17/10/2022
Description: Develop a program that request the user an integer number and shows on the screen a right triangle like
             this one.

"""

number = int(input("Enter a number: "))

for i in range(1, number + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print(" ")