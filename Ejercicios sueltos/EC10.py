"""

Program: EC10.py
Author: Alberto Sánchez Barona
Date: 17/10/2022
Description:  Develop a program to look for the first 20 perfect numbers.

"""

perfect = 0
number = 1
divisor = 0
while perfect <= 5:
    number += 1
    for i in range(1, number // 2 + 1):
        if number % 1 == 0:
            divisor += i
    if number == divisor:
        print(f"The number {number} is perfect.")
    perfect += 1

