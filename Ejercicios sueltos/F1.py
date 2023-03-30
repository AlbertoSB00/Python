"""

Program:        F1.py
Author:         Alberto Sánchez Barona
Date:           20/10/2022
Description:    Develop a function that receives as parameters two numbers and returns one number pointing out the
                following:
                    • 1 If the first number is higher than the second one.
                    • -1 If the second number is higher than the first one.
                    • 0 If both numbers are alike.


"""


def compare_numbers(n1, n2):
    """
    Function:           compare_numbers
    Description:        It receives two numbers and returns one number pointing out.
        :param n1:      First number.
        :param n2:      Second number.
    :return:            A number.
    """
    if n1 > n2:
        number = 1
    elif n1 < n2:
        number = -1
    else:
        number = 0
    return number


result = compare_numbers(5, 7)

match result:
    case 0:
        print("They both are alike")
    case 1:
        print("The first number is higher than the second one.")
    case -1:
        print("The first number is lower than the second one.")

result = compare_numbers(9, 3)
if result == 1:
    print("The first number is higher than the second one.")
elif result == -1:
    print("The first number is lower than the second one.")
else:
    print("They both are alike")