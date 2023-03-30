"""

Program:        F15.py
Author:         Alberto Sánchez Barona
Date:           21/10/2022
Description:    Develop a function that emulates the MOD operator. It receives two parameters and returns the rest of
                the integer division.

"""


def emulate_mod_without_loop(n1, n2):
    cociente = n1 // n2
    divisor = cociente * n2
    result = n1 - divisor
    return result


def emulated_mod_with_loop(n1, n2):
    while n1 >= n2:
        n1 = n1 - n2
    return n1


n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
result = emulate_mod_without_loop(n1, n2)
print(f"The rest of the division is {result}")
result2 = emulated_mod_with_loop(n1, n2)
print(f"The rest of the division is {result2}")
