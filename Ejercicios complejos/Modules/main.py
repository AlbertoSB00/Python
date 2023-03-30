"""

Program:        main.py
Author:         Alberto Sánchez Barona
Date:           02/11/2022
Description:    Main program.

"""

# from date import authenticate_user, read_number, days_of_month, days_of_month
import date as d


def read_number(caption: str, min_number=1, max_number=31, inclusive=True) -> int:
    while True:
        number = int(input(caption))
        if number > 0:
            break

    return number


def main() -> int:
    if not d.authenticate_user():
        print("Authentication Error: The user credentials are not valid. Exiting...")
        exit(1)

    print("User authenticated. Let's go on.")

    min_day = 1
    max_day = 31
    day = read_number("Enter a positive number: ")
    day = int(d.read_number("Enter the day of the month: ", min_day, max_day, True))

    min_month = 1
    max_month = 12
    month = int(d.read_number("Enter the month: ", min_month, max_month, True))

    year = int(input("Enter the year: "))

    print(f"Your date is {day}/{month}/{year}")
    print("Let's check if it is a valid date.")

    days_of_monthh = d.days_of_month(month, year)

    if day > days_of_monthh:
        print(f"Error. Date not valid. The day {day} is not correct for the month {month}.")
        exit(2)

    print(f"The date {day}/{month}/{year} is correct.")
    print("Exiting...")
    exit(0)


if __name__ == "__main__":
    main()
