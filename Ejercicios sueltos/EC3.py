"""

Program: EC3.py
Author: Alberto Sánchez Barona
Date: 05/10/2022
Description: .

"""

user_age = int(input("Enter your age: "))
if user_age < 4:
    print("Free")
if user_age >= 4:
    if user_age < 18:
        print("5€")
if user_age > 18:
    print("18.10€")
print("--------------------------------------------------------------------")
