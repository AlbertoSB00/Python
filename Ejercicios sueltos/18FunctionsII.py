"""

Program:        18FunctionsII.py
Author:         Alberto Sánchez Barona
Date:           19/10/2022
Description:    Develop a program that enter by keyboard the height and the weight of 5 people.
                The weight must be between 45 and 450 kg.
                The height must be between 1.30 and 2.30 m.
                Then, it calculates the BMI and displays on the screen.
                Besides, it shows on the screen the category according to BMI:
                    - Underweight < 18.5
                    - Normal weight 18.5 <= BMI <= 24.9
                    - Overweight 25 <= BMI <= 29.9
                    - Obesity > 30

                BMI = weight / height ** 2

                Task:
                    - Read the valid values of height and weight.      OK
                    - Calculate the BMI.                               OK
                    - Get the category of the BMI.                     OK

"""


def read_number(min_value, max_value, caption):
    """
    Function:               read_number
    Description:            It read a number in a valid range.
    Parameters:
        :param caption:
        :param min_value:   The lower extreme of the range.
        :param max_value:   The upper extreme of the range.
    :return:                The valid number read.
    """
    while True:
        number = float(input(caption))
        if number <= min_value or number >= max_value:
            print("The number is not valid.")
            print(f"The number must be between {min_value} and {max_value}.")
            print("Try it again.")
        else:
            break
    return number


def calculate_bmi(w, h):
    """
    Function:           calculate_bmi
    Description:        It calculates de BMI.
    Parameter:
        :param w:       The weight.
        :param h:       The height.
    :return:            The BMI
    """
    # We can use a function inside another function.
    bmi = w/ h ** 2
    category = category_bmi(bmi)
    print(f"IN FUCTION BMI: The bmi is {bmi} and the category is {category}")
    return bmi


def category_bmi(bmi):
    """
    Function:           category_bmi
    Description:        It calculates the category.
    Parameter:
        :param bmi:     The BMI.
    :return:            The category.
    """
    if bmi < 18.5:
        category = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        category = "Normal weight"
    elif bmi >= 25 and bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"
    return category


for i in range(5):
    weight = read_number(45, 450, f"Enter the weight of person {i + 1} (kg): ")
    height = read_number(1.30, 2.30, f"Enter the height of person {i + 1} (m): ")
    print(f"The weight of the person {i + 1} is {weight}")
    print(f"The height of the person {i + 1} is {height}")

    bmi = calculate_bmi(weight, height)
    category = category_bmi(bmi)
    print(f"The BMI is {bmi}, so your category is {category}")
