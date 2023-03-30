"""

Program: EC9.py
Author: Alberto Sánchez Barona
Date: 14/10/2022
Description:

"""

number = int(input("Enter a positive number: "))

while 1 <= number - 1:
    if number % 2 == 1:
        print(number, end=", ")
    number -= 1
print(number)