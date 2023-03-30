"""

Program:     cuotas.py
Author:      Alberto Sánchez Barona
Date:        03/11/2022
Description: Module for cuotas.

"""

import socios as s


def read_antiquity_year():

    count_year = 0
    antiquity = s.antiquity()
    while True:
        if antiquity >= 12:
            antiquity -= 12
            count_year += 1
        else:
            break

    return count_year


def read_antiquity_month():
    count_month = 0
    if read_antiquity_year() < 12:
        count_month += read_antiquity_year()

    return count_month


def antiquity_bonification_year(category: str):

    count_year = read_antiquity_year()
    bonification_year = 0

    if s.get_category() == "COP":
        if count_year >= 1:
            for i in range(0, count_year):
                bonification_year += 0.5
        else:
            bonification_year += 0

    if s.get_category() == "TEC":
        if count_year >= 1:
            for i in range(0, count_year):
                bonification_year += 1
        else:
            bonification_year += 0

    if s.get_category() == "ACT":
        if count_year >= 1:
            for i in range(0, count_year):
                bonification_year += 2
        else:
            bonification_year += 0

    return bonification_year


def antiquity_bonification_month(category: str):
    count_year = read_antiquity_year()
    bonification_month = 0

    if s.get_category() == "COP":
        if count_year < 1:
            bonification_month = read_antiquity_month() * (0.5 / 12)
        else:
            bonification_month += 0

    if s.get_category() == "TEC":
        if count_year < 1:
            bonification_month = read_antiquity_month() * (1 / 12)
        else:
            bonification_month += 0

    if s.get_category() == "ACT":
        if count_year < 1:
            bonification_month = read_antiquity_month() * (2 / 12)
        else:
            bonification_month += 0

    return bonification_month


def total_bonification():

    return antiquity_bonification_year() + antiquity_bonification_month()


def calculate_initial_fee():

    return s.base_fee(return_category) - total_bonification()


def cuota_neta():

    initial_fee = calculate_initial_fee()
    percentage = s.percentage_initial_fee()
    bonification = total_bonification()
    cuota = initial_fee + percentage + bonification

    return cuota


def main():
    pass


if __name__ == "__main__":
    main()