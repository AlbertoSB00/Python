"""

Program:        date.py
Author:         Alberto Sánchez Barona
Date:           31/10/2022
Description:    Functions.

"""

USERNAME = "usuario"
PASSWORD = "abcd1234@"


# Functions
def authenticate_user(attempts: int = 3) -> bool:
    """
    Function:               authenticate_user
    Description:            It authenticates a valid user.
    Parameters:
        :param attempts:    Maximum number of attempts for a valid user.
    :return:                True if the user is authenticated, False otherwise.
    """

    valid_user = False
    attempt_number = 1

    while not valid_user and attempt_number <= attempts:

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == USERNAME and password == PASSWORD:
            valid_user = True
        else:
            if attempt_number < attempts:
                print("Your username and password are not valid.")
                print(f"Try it again, but remember that you have left {attempts - attempt_number} attempts")
            attempt_number += 1

    return valid_user


def read_number(caption: str, min_value: int, max_value: int, inclusive: bool) -> float:
    """
    Function:               read_number
    Description:            Read a number from the keyboard with in a valid range.
    Parameters:
        :param caption:     The title to document the input.
        :param min_value:   The lowest extreme of the valid range.
        :param max_value:   The highest extreme of the valid range.
        :param inclusive:   If True, the lowest and highest extremes are allowed, otherwise they are not.
    :return:                The number read.
    """

    valid_number = False

    while not valid_number:

        number = float(input(caption))

        if inclusive:
            if number >= min_value and number <= max_value:
                valid_number = True
        else:
            if number > min_value and number < max_value:
                valid_number = True

        if not valid_number:
            print(f"The number {number} is out of range.")
            if inclusive:
                print(f"The number must be between {min_value} and {max_value} both includes.")
            else:
                print(f"The number must be between {min_value} and {max_value} not includes.")

    return number


def is_leap_year(year: int) -> int:
    """
    Function:           is_leap_year
    Description:        It finds out if the year is leap.
    Parameters:
        :param year:    The year to check if it is leap
    :return:            1 if the year is leap, 0 otherwise.
    """

    leap_year = 0

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = 1
        else:
            leap_year = 1

    return leap_year


def days_of_month(month: int, year: int) -> int:
    """
    Function:           days_of_month()
    Description:        Calculate the number of days for a given month and year.
    Parameters:
        :param month:   Number of month to calculate the number of days.
        :param year:    Just in case the month is 2 (february) to find out if the year is leap or not.
    :return:            The number of days of that month and year.
    """

    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            days = 31
        case 4 | 6 | 9 | 11:
            days = 30
        case 2:
            days = 28 + is_leap_year(year)
        case _:
            days = -1

    return days


# Examples
if __name__ == "__main__":
    if authenticate_user():
        print("Access granted")
    else:
        print("User not valid. Exiting...")
        exit(1)

    days = read_number("Enter the days of the month: ", 1, 31, True)
    print(f"1.- {days}")
    days = read_number("Enter the days of the month: ", 10, 30, False)
    print(f"2.- {days}")

    leap = is_leap_year(2024)
    print(f"3.- {leap}")
    leap = is_leap_year(2023)
    print(f"4.- {leap}")
    leap = is_leap_year(2020)
    print(f"3.- {leap}")
    leap = is_leap_year(1902)
    print(f"5.- {leap}")
    leap = is_leap_year(1900)
    print(f"6.- {leap}")

    days = days_of_month(2, 2020)
    print(f"7.- {days}")
    days = days_of_month(2, 2021)
    print(f"8.- {days}")
    days = days_of_month(12, 2022)
    print(f"9.- {days}")
    days = days_of_month(14, 2022)
    print(f"10.- {days}")