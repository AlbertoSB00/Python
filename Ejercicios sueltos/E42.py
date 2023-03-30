"""

Program: E42.py
Author: Alberto Sánchez Barona
Date: 13/10/2022
Description: Develop a program that enters by keyboard 3 numbers 5 times. Each time the numbers must be displayed in
             ascending order.


for i in range(5):
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))

    if n1 < n2 and n2 < n3:
        print("The order is", n1, n2 ,n3)
    elif n2 < n1 and n1 < n3:
        print("The order is", n2, n1 ,n3)
    elif n3 < n1 and n1 < n2:
        print("The order is", n3, n1 ,n2)
    elif n3 < n2 and n2 < n1:
        print("The order is", n3, n2 ,n1)
    elif n1 < n3 and n3 < n2:
        print("The order is", n1, n3 ,n2)
    elif n2 < n3 and n3 < n1:
        print("The order is", n2, n3 ,n1)
    else:
        print("One or more numbers are equals")

"""

for i in range(5):
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))

    if number1 > number2:
        temp = number1
        number1 = number2
        number2 = temp
    if number1 > number3:
        temp = number1
        number1 = number3
        number3 = temp
    if number2 > number3:
        temp = number2
        number2 = number3
        number3 = temp
    print(f"Numbers in forder are: {number1}, {number2}, {number3}")