"""

Program: E4.py
Author: Alberto Sánchez Barona
Date: 29/09/2022
Description: Use the interpreter to declare three integer variables, assigning to each one the number 989 in decimal,
             octal and hexadecimal notation. Display the result on the screen.

"""

integer_number1 = 989
integer_number2 = 989
integer_number3 = 989

integer_decimal = integer_number1
integer_octal = oct(integer_number2)
integer_hexadecimal = hex(integer_number3)
print("The number 989 in decimal is", integer_decimal)
print("The number 989 in octal is", integer_octal)
print("The number 989 in hexadecimal is", integer_hexadecimal)