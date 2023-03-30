"""

Program: E17.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description: Develop a program that enters by keyboard an age and displays a category depending on the
             age: Infancy (0-3), Toddler (4-11), Teenager (12-20), Adult (21-65), Elderly (+65). There are two ways
             to face this problem.

"""

age = int(input("Enter your age: "))
if age >= 0 and age <= 3:
    print("You're infancy.")
elif age >= 4 and age <= 11:
    print("You're toddler.")
elif age >= 12 and age <= 20:
    print("You're teenager.")
elif age >= 21 and age <= 65:
    print("You're adult")
elif age >= 65 and age <= 120:
    print("You're elderly")
elif age > 120:
    print("hmmm")
else:
    print("You're wrong")