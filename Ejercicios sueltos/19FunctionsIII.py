"""

Program:        19FunctionsIII.py
Author:         Alberto Sánchez Barona
Date:           26/10/2022
Description:    Example of parameters with default value.

"""

# Develop a function that receives price, discount and VAT of a product. Then, it returns the net price plus the VAT
# import.
# The VAT by default is 21%
# The discount by default is 10%


def get_total_price(price, discount=0.10, vat=0.21):
    net_price = price - price * discount
    total_price = net_price + net_price * vat
    return total_price


total_price = get_total_price(120)
print(f"The total price is {total_price}")

total_price = get_total_price(65, 0.10)
print(f"The total price is {total_price}")

total_price = get_total_price(69.99)
print(f"The total price is {total_price}")

total_price = get_total_price(3.5, vat=0.04)
print(f"The total price is {total_price}")