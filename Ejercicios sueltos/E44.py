"""

Program: E44.py
Author: Alberto Sánchez Barona
Date: 17/10/2022
Description:  Develop a program that enters by keyboard a number and points out if it is perfect. A number is perfect
              when is equal to the addition of its divisors.

"""

number = int(input("Enter a number: "))
accumulator = 0

for i in range(1, number):
    if number % i == 0:
        accumulator += i
if number == accumulator:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")