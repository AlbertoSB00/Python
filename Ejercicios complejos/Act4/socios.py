"""

Program:     socios.py
Author:      Alberto Sánchez Barona
Date:        03/11/2022
Description: Module for socios.

"""


def get_name():

    name = "a"
    while name != " ":
        name = input("Enter your name (space to leave): ")
        return name


def get_category():

    print("-----------------------------------------")
    print("COP: Cooperante")
    print("TEC: Técnico")
    print("ACT: Activista")
    print("-----------------------------------------")
    category = input("Select your category (COP, TEC, ACT): ")
    match category:
        case "COP":
            return_category = "COP"
        case "TEC":
            return_category = "TEC"
        case "ACT":
            return_category = "ACT"
        case _:
            print(f"ERROR -> {category} is not a category.")
            exit(1)

    return return_category


def base_fee(return_category) -> int:

    category = return_category
    if category == "COP":
        min_fee = 60
        max_fee = 120
        fee = float(input(f"Your base fee is between {min_fee}€ and {max_fee}€. Enter a value: "))
        if fee >= min_fee and fee <= max_fee:
            return_base_fee = fee
        else:
            print(f"Enter a value between {min_fee}€ and {max_fee}€")
            exit(2)
    elif category == "TEC":
        min_fee = 40
        max_fee = 59
        fee = float(input(f"Your base fee is between {min_fee}€ and {max_fee}€. Enter a value: "))
        if fee >= min_fee and fee <= max_fee:
            return_base_fee = fee
        else:
            print(f"Enter a value between {min_fee}€ and {max_fee}€")
            exit(2)
    elif category == "ACT":
        min_fee = 20
        max_fee = 30
        fee = float(input(f"Your base fee is between {min_fee}€ and {max_fee}€. Enter a value: "))
        if fee >= min_fee and fee <= max_fee:
            return_base_fee = fee
        else:
            print(f"Enter a value between {min_fee}€ and {max_fee}€")
            exit(2)

    return return_base_fee


def antiquity():

    month_antiquity = int(input("Introduzca el número de meses que ha sido o es socio: "))
    if month_antiquity < 0:
        print("ERROR -> No puede introducir un mes negativo.")
        exit(3)

    return month_antiquity


def percentage_initial_fee():

    category = return_category
    aportaciones = input("¿Está dispuesto a hacer aportaciones extra? Responda con si o no: ")

    if aportaciones == "si":
        print("Al responder si, se le mostrará las diferentes opciones.")
        print("--------------------------------------------------------")
        print("1.- Apadrinar niños.")
        print("2.- Donación en campaña solitaria.")
        opcion = int(input("Introduzca una opción (1 o 2, 0 para salir: "))
        match opcion:
            case 0:
                exit(4)
            case 1:
                print("Ha elegido apadrinar niños.")
                if get_category() == "COP":
                    fee = base_fee("COP") + (base_fee("COP") * (12.5 / 100))
                else:
                    fee = base_fee() + (base_fee() * (10 / 100))
            case 2:
                print("Ha elegido donario en campaña solitaria.")
                if get_category() == "COP":
                    fee = base_fee("COP") + (base_fee("COP") * (7.5 / 100))
                else:
                    fee = base_fee() + (base_fee() * (5 / 100))
            case _:
                print("ERROR -> Has introducido mal un argumento.")
                exit(5)

        return fee


def main():
    pass


if __name__ == "__main__":
    main()