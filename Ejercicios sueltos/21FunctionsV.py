"""

Program:        21FunctionsV.py
Author:         Alberto Sánchez Barona
Date:           28/10/2022
Description:    Annotations.

What is an annotation? Is a information about the datatype of parameters and value returns of a function.

"""


def get_category(min_age: int = 15, max_age: int = 80) -> str:
    valid_age = False
    while not valid_age:
        age = int(input("Enter your age: "))
        if age >= min_age and age <= max_age:
            valid_age = True
        else:
            print(f"Error. Your age must be between {min_age} and {max_age}.")
    if age >= min_age and age <= min_age + 10:
        category = "teenager"
    elif age > min_age + 10 and age <= max_age - 10:
        category = "adult"
    elif age > max_age - 15 and age <= max_age:
        category = "senior"
    return category


def get_fee(category: str) -> int:
    match category:
        case "teenager":
            fee = 30
        case "adult":
            fee = 40
        case "senior":
            fee = 25
        case _:
            fee = 0
    return fee


name = input("Enter your name: ")
category = get_category(15, 79.5)
fee = get_fee(category)
if fee != 0:
    print(f"Hi, {name}! Your fee es {fee}.")
else:
    print(f"Error. Your category {category} is wrong.")

print("Let's see the get_category() annotations")
print(get_category.__annotations__)