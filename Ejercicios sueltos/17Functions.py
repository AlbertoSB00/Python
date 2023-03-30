"""

Program:        17Functions.py
Author:         Alberto Sánchez Barona
Date:           19/10/2022
Description:    Functions and examples.

"""


# What is a function?
# Functions are statements that are executed under demand in the program. That is, when the programmer needs, it can to
# request to execute the functions.

# What do they work for?
# Big programs can be face better if we split up problem in several task, every one of them is resolved with a function.

# What function are there?
# The language has many many functions. They are known as build in function.
# Objects (in OOP) also have function. They are called methods.
# Programmers can create new functions, call user functions.

# An advantage or function is that they can be reused in many programs. In this case, we can create module (files with
# functions) that we can use in several programs. Modular programming.

# Defining a function.
# A function has:
#   Head -> It contains the function name and the list of parameters.
#   Body -> The statements that form the function.
#   One of them can be the return statement. It returns a value to the point of the program where the function was
#   called.

# Syntax:
#   def <function name>(<par1>, <par2>, <par3>, <...>):
#       [doc string]
#       statement1
#       statement2
#       statement3
#       ...
#       return <value>

# Develop a program that calculated the length of a circumference.

def circumference_length(radio):
    """
    Function:       circumference_length
    Description:    It calculates the length of a circumference and returns it.
    :param radio:   The radio of the circumference.
    :return:        The length of the circumference.
    """
    length = 2 * 3.1415 * radio
    return length


def area_circle(radio):
    """
    Function:       area_circle
    Description:    It calculates the area of a circle.
    :param radio:   The radio of the circle.
    :return:        The area of the circle.
    """
    area = 3.1415 * radio ** 2
    return area


def cylinder_volume(area, height):
    """
    Function:       cylinder_volume
    Description:    It calculates the volume of a cylinder.
    :param area:    The area of the cylinder.
    :param height:  The height of the cylinder.
    :return:        The volume of the cylinder.
    """
    volume = area * height
    return volume


radio = float(input("Enter the radio: "))
height = float(input("Enter the height of the cylinder: "))
length = circumference_length(radio)
area = area_circle(radio)
print(f"The length of a circumference with radio {radio} is {length}.")
print(f"The area of the circle with radio {radio} is {area}.")
volume = cylinder_volume(area, height)
print(f"The volume of the cylinder is {volume}.")

length = circumference_length(0.75)
area = area_circle(0.75)
print(f"The length of a circumference with radio 0.75 is {length}.")
print(f"The area of the circle with radio 0.75 is {area}.")
volume = cylinder_volume(area_circle(0.5), height)
print(f"The volume of the cylinder is {volume}.")


# Parameters:
# Data that functions need to operate.
# In the invocation of the function it could have different values.
# There are two types of parameters:
# 1.- Formal parameter -> Is the parameter defined in the head of the function. It can only be a identifier and it
# behaves as a variable.
# 2.- Real parameter -> Also they are known as arguments. They are the values passed to the function invocation. They
# can be any valid expression (a single literal, a single variable, a more complex expression, even an invocation of
# another function)

# The number and datatype of formal parameters must match with the number and datatypes of the arguments.

# When a function is calling, there is a correspondence among the real parameters (in function head) and arguments
# (in function invocation)
# The value of each argument is copied in the respective formal parameters.