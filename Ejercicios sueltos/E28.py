"""

Program: E28.py
Author: Alberto Sánchez Barona
Date: 10/10/2022
Description: Develop a program that calculates and displays the factorial of a number entered by keyboard.



n = int(input("Enter a number: "))
count = n
result = 0
result1 = 0

while count >= 1:
    result = n * count
    print(f"{n} * {count} = {result}")
    result1 += result
    count -= 1
print("The result is", result1)

"""

number = int(input("Enter a number: "))
if number == 1:
    print(f"The factorial number of {number} is 1")
else:
    counter = number
    factorial = 1
    while counter > 1:
        factorial *= counter
        counter -= 1
    print(f"The factorial of {number} is {factorial}")