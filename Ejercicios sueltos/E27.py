"""

Program: E27.py
Author: Alberto Sánchez Barona
Date: 10/10/2022
Description:  Develop a program that enters by keyboard two positive integers N and M, and then calculates and displays
              the multiple of N lower than M.

"""

n = int(input("Enter a first positive number: "))
while n < 0:
    n = int(input("The number should be positive, try again: "))
m = int(input("Enter a second positive number: "))
while m < 0:
    m = int(input("The number should be positive, try again: "))

multiply = 1
result = 0

if n > m:
    temporal = m
    m = n
    n = temporal

while result < m:
    result = n * multiply
    print(f"{n} * {multiply} = {result}")
    multiply += 1