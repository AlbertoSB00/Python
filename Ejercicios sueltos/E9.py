"""

Program: E9.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description: Develop a program that enters by keyboard the number of worked hours and the salary per hour. Then,
             it calculates and displays on the screen the salary.

"""

worked_hours = float(input("Enter the worked hours: "))
salary_per_hour = float(input("Enter the salary per hour: "))
result = worked_hours * salary_per_hour
print("Your salary is:", result)