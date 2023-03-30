"""

Program: EC7.py
Author: Alberto Sánchez Barona
Date: 07/10/2022
Description: Develop a program that resolves a second grade equation. For it, the conflicts A, B and C are entered by
             keyboard and then, it calculates the possible solution.

"""

a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
c = int(input("Enter a number for c: "))

square_root = b ** 2 - 4 * a * c
if square_root < 0:
    print("The equation has no solution.")

if square_root == 0:
    solution = - b / 2 * a
    print("The operation is", solution)

if square_root > 0:
    solution1 = - b + square_root ** 0.5 / 2 * a
    solution2 = - b - square_root ** 0.5 / 2 * a
    print("The first solution is", solution1, "and the second is", solution2)