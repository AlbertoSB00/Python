"""

Program: 11IfStatement.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description: Example of the if statement. We get into the control structure.


# ----------------------------------------------------------------------------------------------------------------------
#                         ->         Conditional brandes -> If / If else / If else ladder / If elif
# Control Structure       ->         Multiple brandes    -> Match
#                         ->         Loops               -> While / For / Until
# ----------------------------------------------------------------------------------------------------------------------
# If statement
#   Syntax
# If <relational expression>:
#
#       statement 1
#       statement 2
#       ...
#
# First statement out of If
#
# How does it work? If the relational or logical expression is True, the statement inside if are executed.
# If False, there are not executed.
# We consider a statement is inside the if, if they are writer with and indent.

# Enter a number by keyboard and show if it is even.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("1.- The number is even.")
print("1.- The entered number is:", number)
print("--------------------------------------------------------------------")

# Enter an age by keyboard and show if it is an adult or boy.
age = int(input("2.- Enter your age: "))
if age >= 18:
    print("2.- You are an adult.")
if age < 18:
    print("2.- You are an boy.")
print("--------------------------------------------------------------------")

# Clause else
# We sometimes need to execute some statement just in case the relational or radical expression in if statement is false
# We can add an else clause to the if statement. So, now we have two blocks of statement. The former for the true part
# or if and the letter for the false part of is (else clause).
# Only one bloc is executed.
# Syntax
# If <relational expression>:
#    statement 1
#    statement 2
#    ...
# else:
#    statement 1
#    statement 2
#    ...

number = int(input("3.- Enter a number: "))
if number % 2 == 0:
    print("3.- The number", number, "is even.")
else:
    print("3.- The number", number, "is odd.")
print("--------------------------------------------------------------------")

# Develop a program that store a password in a variable. Then, it enters by keyboard the password and check if the
# password is right or not.
password = "abcd1234"
user_password = input("4.- Enter the password: ")
if password == user_password:
    print("4.- The password is correct.")
else:
    print("4.- The password isn't correct.")
print("--------------------------------------------------------------------")

# Nested if
# If statement can be nested: That means we can include an If statement inside de part true or false (else clause)
# There is no limit. We can include so many if inside other if as we need.

# Enter by keyboard two marks. If they both are passed, we will calculate the average mark. If one of them, or both
# are not passed, we will show a message printing out you want retake the subject.
mark1 = float(input("5.- Enter the first mark: "))
mark2 = float(input("5.- Enter the second mark: "))
if mark1 >= 5 and mark2 >= 5:
    average = (mark1 + mark2) / 2
    print("5.- Your average is", average)
else:
    if mark1 < 5:
        print("5.- You must retake the first subject.")
    if mark2 < 5:
        print("5.- You must retake the second subject.")
    print("5.- You should study a bit more. You have failed at least one subject.")
print("--------------------------------------------------------------------")

"""

# If elif ladder.
# Let's suppose we enter a mark by keyboard, and then we show the grade.

mark = float(input("6.- Enter your mark: "))
if mark < 5:
    print("6.- You're failed.")
else:
    if mark < 6:
        print("6.- Your grade is C")
    else:
        if mark < 7:
            print("6.- Your grade is B-")
        else:
            if mark < 9:
                print("6.- Your grade is B")
            else:
                if mark <= 10:
                    print("6.- Your grade is A")
print("6.- Your mark is", mark)
print("--------------------------------------------------------------------")

# Much better with if elif.
if mark < 5:
    print("7.- You have failed.")
elif mark < 6:
    print("7.- Your grade is C")
elif mark < 7:
    print("7.- Your grade is B-")
elif mark < 9:
    print("7.- Your grade is B")
elif mark <= 10:
    print("7.- Your grade is A")
else:
    print("7.- You are wrong")
print("7.- Your mark is", mark)
print("--------------------------------------------------------------------")
