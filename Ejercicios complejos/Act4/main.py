"""

Program:     main.py
Author:      Alberto Sánchez Barona
Date:        03/11/2022
Description: This is the main program.

"""

import socios as s
import cuotas as c


def main():

    name = s.get_name()
    category = s.get_category()
    base_fee = s.base_fee(category)
    antiquity = s.antiquity()
    initial_fee = s.percentage_initial_fee()
    neta_fee = c.cuota_neta()

    print(f"Hi, {name}.")
    print(f"Your category is: {category}")
    print(f"Your base fee is: {base_fee}")
    print(f"Your antiquity is: {antiquity}")
    print(f"Your initial fee is: {initial_fee}")
    print(f"Your neta fee is: {neta_fee}")


if __name__ == "__main__":
    main()