"""

Program: E32.py
Author: Alberto Sánchez Barona
Date: 10/10/2022
Description: Develop a program that displays on the screen the squares and cubes of the numbers there are between two
            entered by keyboard.

"""

n = int(input("Enter a first number: "))
m = int(input("Enter a second number: "))
count = n

while count <= m:
    squares = count ** 2
    print(f"{count}^2 = {squares}")
    cubes = count ** 3
    print(f"{count}^3 = {cubes}")
    count += 1