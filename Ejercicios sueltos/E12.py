"""

Program: E12.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description: Develop a program that enters by keyboard the weight (in Kg) and the height (in metres). Then, it
             calculates the body-mass index. Finally, it displays on the screen the statement Your body-mass index
             is <bmi>, where <bmi> is the body-mass index calculated with two decimals digits.

"""

weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in metres): "))
body_mass = weight / height**2
print(f"Your body-mass index is {body_mass:{2}.{2}f}, where {body_mass:{2}.{2}f} is the body-mass index calculated "
      f"with two decimals digits.")