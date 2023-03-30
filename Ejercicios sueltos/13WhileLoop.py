"""

Program: 13WhileLoop.py
Author: Alberto Sánchez Barona
Date: 06/10/2022
Description: Example of while loops.

notes:

for counter = initial value logical expression increment expression -> if true, new iteration is executed.
                                                                        if false, the loop finished

while logical expression
    statement 1
    statement 2
    statement 3
    ...
    go up

do
    statement 1
    statement 2
    statement 3
    ...
while logical expression

do
    statement 1
    statement 2
    statement 3
    ...
until logical expression

"""

# W
# While loop syntax
# While <logical expression>:
#   statement1
#   statement2
#   ...
# else:
#   statement1
#   statement2
#   ...

# Enter by keyboard an age that must be between 18 and 65
age = 0
min_age = 18
max_age = 65
while age < min_age or age >max_age:
    age = int(input("Enter your age: "))
    if age < min_age or age > max_age:
        print("Your age is wrong. Try it again.")
print("Your age is", age)



# Enter a password by keyboard with 3 attempts at maximum. In the end, it must show how many attempts the user has
# needed to access and if it got it.
password = "abcd1234"
user_pass = " "
max_attempts = 3
current_attempt = 1
while user_pass != password and current_attempt <= max_attempts:
    user_pass = input(f"Enter the password (Attempt {current_attempt}/{max_attempts}): ")
    if user_pass == password:
        print("The password is true.")
        print("You needed", current_attempt, "attempts.")
    if current_attempt >= max_attempts:
        print("To much tries")
    current_attempt = current_attempt + 1

# Menu
# What is a menu? A menu is a set of options where user has to choose one of them. Each menu option has an associated
# action. Then, the action that belongs to the chosen options will be executed.

option = 0
while option != 5:
    print("\t\t Options Menu")
    print("\t\t-------------")
    print("\t1.- Create a new user")
    print("\t2.- Update user properties")
    print("\t3.- Convert an user as administrator")
    print("\t4.- Delete an user")
    print("\t5.- Exit")
    option = int(input("Enter an option: "))
    match option:
        case 1:
            print("You are creating a new user")
        case 2:
            print("You are updating an user")
        case 3:
            print("You are converting an user as administrator")
        case 4:
            print("You are deleting an user")
        case 5:
            print("Exiting")
        case _:
            print("Wrong option. It must be between 1 and 5")
    input("Press enter to continue.")