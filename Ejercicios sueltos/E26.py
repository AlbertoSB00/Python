"""

Program: E31.py
Author: Alberto Sánchez Barona
Date: 07/10/2022
Description: Develop a program that displays the list of an interest and the capital accumulated produced every year
             by an initial capital C, charge with a yield Y for N years. The interest got annually is calculated
             with the formula: I=C*Y/100 The capital is increased with the interest produced every year.

"""

counter = 1
year = int(input("Enter the number of years: "))
initial_capital = float(input("Enter the initial capital: "))
yield_percent = float(input("Enter the yield: "))
capital_counter = 0
while counter <= year:
    capital = (initial_capital * yield_percent) / 100
    capital_counter += capital
    print(f"Year {counter} you got {capital_counter} €")
    counter += 1