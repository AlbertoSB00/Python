"""

Program: E13.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description: Develop a program that enters by keyboard two integer numbers and displays on the screen the statement <n>
             divided by <m> results a quotient of <c> y the rest is <r>, where <n> and <m> son the numbers entered,
             <c> is the quotient and <r> is the rest respectively.

"""

integer1 = int(input("Enter the first integer: "))
integer2 = int(input("Enter the second integer: "))

divided = integer1 / integer2
rest = integer1 % integer2

print(f"The statement {integer1} divided by {integer2} results a quotient of {divided} and the rest is {rest} where "
      f"{integer1} and {integer2} are the numbers entered, {divided} is the quotient and {rest} is the rest "
      f"respectively.")