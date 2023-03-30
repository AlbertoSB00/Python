"""

Program: EC8.py
Author: Alberto Sánchez Barona
Date: 10/10/2022
Description: Develop a program that requests the user and integer number and shows on the screen if the number is a
             prime number or not.

Esta forma de hacerlo está mal.

number = int(input("Enter a number: "))
result1 = number % 2
result2 = number % 3
result3 = number % 5
result4 = number % 7
result5 = number % 11

if result1 == 0:
    print(f"The number {number} is not prime, is a 2 divisor.")
elif result2 == 0:
    print(f"The number {number} is not prime, is a 3 divisor.")
elif result3 == 0:
    print(f"The number {number} is not prime, is a 5 divisor.")
elif result4 == 0:
    print(f"The number {number} is not prime, is a 7 divisor.")
elif result5 == 0:
    print(f"The number {number} is not prime, is a 11 divisor.")
else:
    print(f"The number {number} is prime.")

"""

number = int(input("Enter a number: "))
square_root = number ** 0.5
is_prime = True
while square_root >= 2:
    if number % square_root == 0:
        print(f"The number {number} is not prime.")
        is_prime = False
    square_root -= 1
if is_prime:
    print(f"The number {number} is prime.")