MAX_MEMORY = 64
MEMORY_BANK = 4
MIN_SIZE_MODULE = 4

class NegativeMoneyException(Exception):
    """
    Class:          NegativeMoneyException
    Description:    It raises when the user enters a negative amount of money.
    """
    pass


class MenuOptionNotValidException(Exception):
    """
    Class:          MenuOptionNotValidException
    Description:    It raises when the user enters a menu option not valid.
    """
    pass


class MoneyAvaibleExceedException(Exception):
    """
    Class:          MoneyAvaibleExceedException
    Description:    It raises when the user choose a component the customer has choosen and aceeds the money they have left.
    """
    pass

class MemoryAmountNotValidException(Exception):
    """
    Class:          MemoryAmountNotValidException
    Description:    It raises when customer enters on amount of memory not valid.
    """
    pass


def question_yes_no(question):

    valid_response = False

    while not valid_response:

        response = input(question + " (Y/n)? ")

        if response == "" or response.upper() == "Y" or response.upper() == "N":
            valid_response = True
        else:
            print("ERROR -> You must answer [y]es or [n]ot")
            print("Try it again...")

    # End of while loop

    if response == "" or response.upper() == "Y":
        return True
    else:
        return False

# End of the function question_yes_no(question)


def read_money_limit(min_money):
    """
    Function:           read_money_limit
    Description:        Read by keyboard the money limit the custormers set.
    Parameters:
        min_money:      The minimum amount of money neccesary to build a computer.
    Returns:            The money limit.
    """

    valid_money = False

    while not valid_money:

        try:
            money_limit = int(input("Enter how much money you are willing to expense in your computer: "))
            if money_limit < 0:
                raise NegativeMoneyException
            if money_limit <= min_money:
                raise MoneyAvaibleExceedException("The money you are willing to expense is not enough for the cheapest PC.")

        except ValueError:
            print("ERROR -> It has to be a number.")

        except MoneyAvaibleExceedException as maee:
            print(maee.__str__())

        except NegativeMoneyException:
            print("The amount of money cannot be negative.")
            print("Try it again...")

        else:
            valid_money = True
        
        # End while loop
    
    return money_limit
# End function read_money_limit()


def read_mainboard(money_remaining):
    """
    Function:           read_mainboard
    Description:        Show a menu with the mainboards.
    Parameters:         The money limit.
    Returns:            The mainboard selected.
    """
    # Terminar esto en todas las funciones---------------------------------------------------
    try:

        if money_remaining < 300:
            raise MoneyAvaibleExceedException("You don't have enough money for the cheapest mainboard.")
    
    except MoneyAvaibleExceedException as maee:
        price(maee.__str__())
        return "", 0
    # Terminar esto en todas las funciones---------------------------------------------------


    valid_option = False
    
    while not valid_option:
        print("Mainboards available")
        print("--------------------")
        print("1.- Z790 -> 400€")
        print("2.- H610M -> 350€")
        print("3.- B660M -> 325€")
        print("4.- H81M -> 300€")

        try:

            option = int(input(f"Enter a number of mainboard. You have {money_remaining}€ left: "))
            match option:
                case 1:
                    model_mainboard = "Z790"
                    price = 400
                case 2:
                    model_mainboard = "H610M"
                    price = 350
                case 3:
                    model_mainboard = "B660M"
                    price = 325
                case 4:
                    model_mainboard = "H81M"
                    price = 300
                case _:
                    raise MenuOptionNotValidException("Enter a valid option.")
            
            if price > money_remaining:
                raise MoneyAvaibleExceedException(f"Your mainboard {model_mainboard} is too expensive. It cost {price}€ and you only have {money_remaining}€")

        except ValueError:
            print("Enter a valid number. Try it again...")

        except MenuOptionNotValidException as monve:
            print(monve.__str__())
        
        except MoneyAvaibleExceedException as maee:
            print(maee.__str__())
        
        else:
            valid_option = True

    return model_mainboard, price


def cpu_mainboard_compatible(model_mainboard, model_cpu):
    """
    Function:               cpu_mainboard_compatible
    Description:            It checks if a cpu a mainboard are compatible.
    Parameters:
        model_mainboard:    The model of mainboard.
        model_cpu:          The model of cpu.
    Return:                 If are compatible or not.
    """

    compatible = True
    if model_cpu == "Z9" and model_mainboard != "Z790":
        compatible = False
    
    if model_mainboard == "H81M" and model_cpu != "G5":
        compatible = False

    return compatible


def read_cpu(money_remaining):
    """
    Function:               read_cpu
    Description:            It enters by keyboard a model of cpu.
    Parameters:
        money_remaining:    The money available
    Return:                 The model of cpu 
    """

    valid_option = False
    while not valid_option:
        print("CPU models")
        print("--------------------------------")
        print("Zorin models | Goldfinger models")
        print("1.- Z5\t250€ | 4.- G5\t270€")
        print("2.- Z7\t450€ | 5.- G7\t420€")
        print("3.- Z9\t700€ | 6.- G9\t670€")

        try:

            option = int(input(f"Enter a number to choose the model you want. You have {money_remaining}€ left: "))

            match option:
                case 1:
                    model_cpu, price_cpu = "Z5", 250
                case 2:
                    model_cpu, price_cpu = "Z7", 450
                case 3:
                    model_cpu, price_cpu = "Z9", 700
                case 4:
                    model_cpu, price_cpu = "G5", 275
                case 5:
                    model_cpu, price_cpu = "G7", 420
                case 6:
                    model_cpu, price_cpu = "G9", 670
                case _:
                    raise MenuOptionNotValidException("The number of cpu model is not valid.")
        
            if price_cpu > money_remaining:
                raise MoneyAvaibleExceedException(f"Your mainboard {model_cpu} is too expensive. It cost {price_cpu}€ and you only have {money_remaining}€")

        except ValueError:
            print("The number of model entered is not valid. Try it again...")

        except MenuOptionNotValidException as monve:
            print(monve.__str__())
            print("Try it again...")
        
        except MoneyAvaibleExceedException as maee:
            print(maee.__str__())

        else:
            valid_option = True

    return model_cpu, price_cpu


def get_ram_price(modules, capacity):

    match capacity:
        case "16GB":
            unit_price = 100
        case "8GB":
            unit_price = 60
        case "4GB":
            unit_price = 40
        case _:
            unit_price = 0
    
    return modules * unit_price


def read_ram(money_remaining):
    
    valid_number = False

    while not valid_number:
        
        try:
            ram = int(input(f"Enter how much memory do you want (4-64). Remember you have left {money_remaining}€ left: "))
            
            if ram < MIN_SIZE_MODULE or ram > MAX_MEMORY:
                raise MemoryAmountNotValidException(f"The amount of RAM cannot be greater than {MAX_MEMORY}.")
            
            if ram % MIN_SIZE_MODULE != 0:
                raise MemoryAmountNotValidException(f"The amount of RAM must be a multiply of {MIN_SIZE_MODULE}.")
            
            # We calculate the neccessary memory modules.
            modules = 0

            ram_16 = ram // 16
            ram = ram % 16
            modules += ram_16

            ram_8 = ram // 8
            ram = ram % 8
            modules += ram_8

            ram_4 = ram // 4
            ram = ram % 4
            modules += ram_4

            if modules > 4:
                raise MemoryAmountNotValidException(f"You only have {MEMORY_BANK} memory banks and you have choosen memory for {modules} modules.")
            
            total_ram = 0

            if ram_16 > 0:
                total_ram = get_ram_price(ram_16, "16GB")
            if ram_8 > 0:
                total_ram += get_ram_price(ram_8, "8GB")
            if ram_4 > 0:
                total_ram += get_ram_price(ram_4, "4GB")

            if money_remaining < total_ram:
                raise MoneyAvaibleExceedException(f"You don't have enough money for so much memory, you need {total_ram}€ and you have {money_remaining}€ left.")            

        except ValueError:
            print("The value entered is not valid. Try again...")

        except MemoryAmountNotValidException as manve:
            print(manve.__str__())
            print("Try it again...")

        except MoneyAvaibleExceedException as maee:
            print(maee.__str__())
            print("Try it again...")
        
        else:
            valid_number = True
    # End while loop

    return ram_16, ram_8, ram_4, total_ram


def read_hd(money_remaining):
    
    valid_number = False
    while not valid_number:
        try:
            print("Hard Disks")
            print("---------------------")
            print("1.- SSD Sata III 1 TB -> 100€")
            print("2.- SSD NVMe 512 GB -> 150€")

            option = int(input(f"Enter the number of HD you want. (Remember you have {money_remaining}€ left): "))
            if option < 1 or option > 2:
                raise MenuOptionNotValidException("The option enter only can be 1 or 2.")
            
            if option == 1:
                model_hd = "SSD Sata III 1 TB"
                price_hd = 100
            else:
                model_hd = "SSD NVMe 512 GB"
                price_hd = 150

            if money_remaining < price_hd:
                raise MoneyAvaibleExceedException(f"You don't have enough money for the HD chose. Your HD cost {price_hd} and you have {money_remaining}€ left.")

        except ValueError:
            print("The option entered is not valid. Try it again...")
        
        except MenuOptionNotValidException as monve:
            print(monve.__str__())
            print("Try it again...")
        
        except MoneyAvaibleExceedException as maee:
            print(maee.__str__())
            print("Try it again...")
        
        else:
            valid_number = True
    
    return model_hd, price_hd


def read_case(money_remaining):
    valid_number = False
    
    while not valid_number:
        print("Case for your PC")
        print("----------------")
        print("1.- Case with 450w -> 45€")
        print("2.- Case with 500w -> 55€")
        print("3.- Case with 600w -> 60€")

        try:

            option = int(input(f"Enter the number of case you want for your PC. (Remember you have {money_remaining}€ left): "))

            if option < 1 or option > 3:
                raise MenuOptionNotValidException("The option entered is not valid. You must enter an option between 1 and 3.")
            
            match option:
                case 1:
                    model_case = "450w"
                    price_case = 45
                case 2:
                    model_case = "500w"
                    price_case = 50
                case 3:
                    model_case = "600w"
                    price_case = 60
                case _:
                    model_case = ""
                    price_case = 0

            if money_remaining < price_case:
                raise MoneyAvaibleExceedException(f"The case you have chosen is too expensive. It cost {price_case}€ and you have {money_remaining}€ left.")
        
        except ValueError:
            print("The option entered is not valid. Try it again...")
        
        except MenuOptionNotValidException as monve:
            print(monve.__str__())
            print("Try it again...")
        
        except MoneyAvaibleExceedException as maee:
            print(maee.__str__())
            print("Try it again...")
        
        else:
            valid_number = True

    return model_case, price_case


def read_shipping(money_remaining, total_pc):
    valid_number = False
    while not valid_number:
        try:
            
            print("Shipping")
            print("--------")
            print("1.- Peninsula -> 0.5%")
            print("2.- Canary Islands and Balears Islands -> 0.75%")
            print("3.- European Union -> 1%")

            option = int(input("Enter the place to send the PC: "))

            if option < 1 or option > 3:
                raise MenuOptionNotValidException("The option is not valid, it must be between 1 and 3.")
            
            match option:
                case 1:
                    perc_shipping = 0.005
                case 2:
                    perc_shipping = 0.0075
                case 3:
                    perc_shipping = 0.01
                case _:
                    perc_shipping = 0

            total_shipping = total_pc * perc_shipping
            if money_remaining < total_shipping:
                raise MoneyAvaibleExceedException(f"You don't have enough money for shipping. You need {total_shipping}€ and you have {money_remaining}€ left.")

        except ValueError:
            print("The option entered is not valid. Try it again...")
        
        except MenuOptionNotValidException as monve:
            print(monve.__str__())
            print("Try it again...")
        
        except MoneyAvaibleExceedException as maee:
            print(maee.__str__())
            print("Try it again...")
        
        else:
            valid_number = True
    
    return total_shipping