"""

Program:        F16.py
Author:         Alberto Sánchez Barona
Date:           25/10/2022
Description:    Develop a function that emulates the logical operator XOR. For it, it receives two logical parameters
                and returns the result.

"""


def xor(par1, par2):
    if par1 and par2:
        result = False
    elif par1 and not par2:
        result = True
    elif not par1 and par2:
        result = True
    elif not par1 and not par2:
        result = False
    else:
        result = "Wrong parameter, enter True or False"
    return result


def xorv2(par1, par2):
    return (par1 or par2) and not (par1 and par2)


par1 = input("Enter True or False: ")
par2 = input("Enter, again, True or False: ")

result = xor(par1, par2)
print(f"The result of {par1} | {par2} | {result}")
result2 = xorv2(par1, par2)
print(f"The result of {par1} | {par2} | {result2}")