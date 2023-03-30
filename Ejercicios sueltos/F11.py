"""

Program:        F11.py
Author:         Alberto Sánchez Barona
Date:           21/10/2022
Description:    Develop a function that converts a decimal number in binary one and another one that converts a binary
                number in a decimal one.

"""


def decimal_to_binary(num):
    if num == 0:
        num = "0"
    elif num == 1:
        num = "1"
    else:
        result = ""
        while num // 2 > 0:
            rest = num % 2
            result = str(rest) + result
            num = num // 2
        else:
            rest = num % 2
            result = str(rest) + result
        return result


def binary_to_decimal(num):
    return int(num, 2)


binary = decimal_to_binary(215)
print(f"The number {215} in binary is {binary}")
decimal = binary_to_decimal(binary)
print(f"The number {binary} in decimal is {decimal}")
