"""

Program:        20FunctionsIV.py
Author:         Alberto Sánchez Barona
Date:           26/10/2022
Description:    Scope and visibility.

"""

# There are tho features about variables that tell us when we can use then.
# Scope -> Part of the program where a variable exists.
# Visibility -> Part od the program where a variable is visible and accessible.


def triangle_area(base, height):
    print(f"F: The value of base is {base}")
    print(f"F: The value of height is {height}")
    area = b * height / 2
    return area


b = 10
height = 3.5
area = triangle_area(b, height)
print(f"The area is {area}")