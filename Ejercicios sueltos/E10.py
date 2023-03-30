"""

Program: E10.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description: Develop a program that enters by keyboard a positive integer number and then displays the addition of
             integer numbers from 1 to the entered number. This addition can be calculated with the following
             expression: (n*(n+1))/2

"""

number = int(input("Enter a positive integer number: "))
result = (number * (number + 1)) / 2
print("The result is: ", result)