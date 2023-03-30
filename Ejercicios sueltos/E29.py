"""

Program: E29.py
Author: Alberto Sánchez Barona
Date: 10/10/2022
Description: Develop a program that enters by keyboard 15 times a number and displays a message on the screen about if
            the number is divisible by 2, by 3 or by none of them.

"""

n = int(input("Enter a number: "))
count = 1

while count <= 15:
    by2 = n % 2
    by3 = n % 3
    if by2 == 0 and by3 == 0:
        print(f"The number {n} is divisible by 2 and 3")
        n = int(input("Enter a number: "))
        count += 1
    if by2 == 0:
        print(f"The number {n} is divisible by 2")
        n = int(input("Enter a number: "))
        count += 1
    if by3 == 0:
        print(f"The number {n} is divisible by 3")
        n = int(input("Enter a number: "))
        count += 1
    if by2 != 0 and by3 != 0:
        print(f"The number {n} is not divisible by 2, 3 or 2 and 3")
        n = int(input("Enter a number: "))
        count += 1