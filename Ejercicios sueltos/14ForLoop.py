"""

Program: 14ForLoop.py
Author: Alberto Sánchez Barona
Date: 10/10/2022
Description: Example of use for loops.

"""

# Typically the for loop has tje following syntax.
# for <counter> = <initial value> to <final value> [<step expression>]
#   statement1
#   statement2
#   ...
# end for

# The syntax has got:
# <counter>: An integer variable initialized with the <initial value>. It is used to control the number of iterations.
# <final value>: The final value for the <counter> variable.
# <step expression>: A value to increase or decrease the <counter> variable.

# How it works:
# 1.- The <counter> variable is initialized with the <initial value>
# 2.- It is checked if <counter> variable has a value lower than <final value>
# 3.- If True -> A new iteration is executed. All the statement in for loop are executed.
# 4.- If False -> The for loop finished and the flow of program continues by the following statement after for loop.
# 5.- When a iteration is executed, the <counter> variable is increased with the value of <step expression> or 1 if it
#     is emitted.

# This way of operations can be simulated with while loop.
# For the last years, the evolution of programming languages has taken to the use of compound data structures.
# For example: {arrays, dictionaries, lists...}
# For these type os structure python has got the for loop with the following syntax.
# for <variable> in <list>:
#   statement1
#   statement2
#   ...
# else:
#   statement1
#   statement2
#   ...

# We can generate a list with the range() function.
# range([start, ] end [,step1])
# start -> The initial value of the range. If it is omited is 1.
# end -> The final value of range.
# step -> The increment, or decrement, of the <variable> is each iteration.

print("1.- The simplest way of for loop.")
print("1.- Display the first 10 numbers.")
for i in range(10):
    print("1.- The value of i is:", i)
else:
    print("1.- The final value of i:", i)
print("------------------------------------------------")

print("2.- The range() function starts with 10 and finished with 20")
for i in range(10,21):
    print("2.- The value of i is:", i)
else:
    print("2.- The final value of i:", i)
print("------------------------------------------------")

print("3.- The range() function with a step expression.")
for i in range(10, 41, 2):
    print("3.- The value of i is:", i)
else:
    print("3.- The final value of i:", i)
print("------------------------------------------------")

print("4.- The range() function with negative step expression.")
for i in range(20, 5, -1):
    print("4.- The value of i is:", i)
else:
    print("4.- The final value of i:", i)
print("------------------------------------------------")