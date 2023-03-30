"""

Program: 15BreakAndContinueStatement.py
Author: Alberto Sánchez Barona
Date: 14/10/2022
Description: Example of use for break and continue statement.



# The break and the continue statement can only be used in inside a loop.

# Break -> Exit from any loop no matter if the logical expression is true or false. All statement below break are not
#          executed so the iteration can be incomplete.

# Continue -> It force to revalue again the logical expression of the loop. Any statement below the continue statement
#             is not executed in that iteration, but it could be executed in the next iteration.

# Example: Enter a number by keyboard and displays if the number is prime. A number is prime if it has no divisor
#          lower than square root.

number = int(input("Enter a number: "))
square_root = int(number ** 0.5)

for i in range(2, square_root):
    print(f"Evaluating {i}")
    if number % i == 0:
        break
    else:
        print(f"The number {i} is not a divisor of {number}")

if i == square_root - 1:
    print(f"The number {number} is prime.")
else:
    print(f"The number {number} is not prime.")



# We can simulate the loop do .. while and do .. until

# Enter by keyboard numbers until one negative and for each of them displays if it is odd or even.
while True:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
    if number < 0:
        break
# End of while loop.

"""

# Enters number by keyboard until you enter 0. For each number display if it is even or odd except the negative numbers.
while True:
    number = int(input("Enter a positive number (0 to exit): "))
    if number < 0:
        continue
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
    if number == 0:
        break
# End of while loop