"""

Program: 01DataTypeDocs.py
Author: Alberto Sánchez Barona
Date: 22/09/2022
Description: With this program we will se how to manage the different datatypes Python has.

"""

# Integers
integer_number = 320
print(integer_number)

# Integers numbers in octal numbering system.
integer_octal = 0o75
print(integer_octal)

# Integers numbers in hexadecimal numbering system.
integer_hex = 0xfa
print(integer_hex)

# Integers numbers in binary numbering system.
integer_binary = 0b10000001
print(integer_binary)

# Conversions of numbering system.
integer_octal = oct(integer_number)
integer_hex = hex(integer_number)
integer_binary = bin(integer_number)
print(integer_octal)
print(integer_hex)
print(integer_binary)

# Float is the datatype for real numbers.
pi = 3.14159
print("The PI number is", pi)

# What is the smaller size of a virus.
# 5.5 nm
smallest_virus = 5.5e-9

# IBM is building chips with 2.6 nm of transistor size.
smallest_transistor = 0.26e-10
print("Virus and transistors", smallest_virus, smallest_transistor)

# The diameter of the Earth.
diameter_earth = 4e4
print("The diameter of the earth is", diameter_earth)

# Stings.
# Strings enclosed by double quotes.
my_name = "Alberto Sánchez"
# Strings enclosed by single quotes.
your_name = 'Paco Sánchez'
print("My name is", my_name, "and the yours is", your_name)

# Stings with single and double quotes inside.
my_name = "I'm Javier"
print("My now name is", my_name)
my_name = 'I"m Pedro'
print("My now name is", my_name)

# Escape character is \
my_name = 'I\'m Peter'
print("My new name now is", my_name)

# Backslash as a normal character
profile_windows = "C:\\Users\\Usuario"
print("My profile in Windows is in", profile_windows)

# We add tabs in show information in a table
header = "Nif\tName\tBirthday\tGroup"
header2 = "---\t----\t--------\t-----"
print(header)
print(header2)

# Multiline strings
several_lines = """
This is a string
with four lines
and I have done it with
the double quotes"""
print(several_lines)

several_lines = '''
However, we can
do it with single quotes
as well'''
print(several_lines)

length_profile_windows = len(profile_windows)
print("The length of profile_windows is", length_profile_windows)
length_several_lines = len(several_lines)
print("The several lines sting has", length_several_lines, "characters")

# Booleans type
exist_user = False
print("The user exist?", exist_user)

# Conversions datatype
integer_number = 3
float_number = 2.75
sum_numbers = integer_number + float_number
print("The results is", sum_numbers)

str_number = "34"
integer_number = 8
# Error -> sum_str_integer = integer_number + str_number
# Error -> sum_str_integer = str_number + integer_number
# Good with explicit conversion.
sum_str_integer = int(str_number) + integer_number
print("The sum is", sum_str_integer)

# Not always is possible the conversion
str_number = "34.2"
integer_number = 8
# Error -> sum_str_integer = int(str_number) + integer_number
# print("The sum is", sum_str_integer)

sum_str_integer = float(str_number) + integer_number
print("The sum is", sum_str_integer)

# How can we find the data type of any data.
print(type(str_number))
print(type(integer_number))
print(type(sum_str_integer))