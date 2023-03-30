"""
Program:        Act5-Corregida
Author:         Alberto Sánchez Barona
Date:           10/11/2022
Description:    According the formulation in GlobalActivity05.pdf
"""

from modul import read_money_limit, read_mainboard, cpu_mainboard_compatible, read_cpu, read_ram, read_hd, read_case, read_shipping,  question_yes_no


def main():

    while True:

        try:
            
            # Nombre
            name = input("Enter the customer's name: ")
            if name == "":
                break

            # Address
            address = input("Enter the customer's address: ")

            # Money limit
            min_money = 735
            money_limit = read_money_limit(min_money)
            money_remaining = money_limit
            total_pc = 0


            # Mainboard & CPU
            cpu_and_mainboard_valid = False
            mainboard_valid = False
            cpu_valid = False

            while not mainboard_valid or not cpu_valid:

                # Mainboard
                if not mainboard_valid:
                    model_mainboard, price_mainboard = read_mainboard(money_remaining)
                    
                    # Terminar esto en todas las funciones---------------------------------------------------
                    if model_mainboard == "":
                        money_remaining = read_money_limit(min_money)
                    # Terminar esto en todas las funciones---------------------------------------------------

                    money_remaining -= price_mainboard
                    print(f"Your mainboard is {model_mainboard}. It cost {price_mainboard}€. So, you have left {money_remaining}€")

                # CPU
                if not cpu_valid:
                    model_cpu, price_cpu = read_cpu(money_remaining)
                    money_remaining -= price_cpu
                    print(f"Your CPU is {model_cpu}. It cost {price_cpu}€. So, you have left {money_remaining}€")

                # Compare Mainboard & CPU
                if not cpu_mainboard_compatible(model_mainboard, model_cpu):
                    print(f"Your mainboard {model_mainboard} and CPU {model_cpu} are not compatible.")
                    cpu_valid = False
                    mainboard_valid = False
                    if question_yes_no("Do you want to change mainboard"):
                        cpu_valid = True
                        money_remaining += price_mainboard
                    elif question_yes_no("Do you want to change cpu"):
                        mainboard_valid = True
                        money_remaining += price_cpu

                else:
                    mainboard_valid = cpu_valid = True
            # Ends while loop

            total_pc += price_mainboard + price_cpu

            # Memory
            ram_16, ram_8, ram_4, total_ram = read_ram(money_remaining)
            money_remaining -= total_ram
            print(f"You need {ram_16} modules of 16GB, {ram_8} modules of 8GB and {ram_4} modules of 4 GB. The total memory cost is {total_ram}€. You have {money_remaining}€ left")

            total_pc += total_ram

            # Hard disk
            model_hd, price_hd = read_hd(money_remaining)
            money_remaining -= price_hd
            print(f"Your HD is {model_hd} and cost {price_hd}€. So, you have {money_remaining}€ left.")

            total_pc += price_hd

            # Case
            model_case, price_case = read_case(money_remaining)
            money_remaining -= price_case
            print(f"Your case is {model_case} and cost {price_case}€. So, you have {money_remaining}€ left.")

            total_pc += price_case

            # Shipping
            total_shipping = read_shipping(money_remaining, total_pc)
            print(f"The PC was {total_pc}€ we have to include the shipping, so is {total_shipping}€")

        except KeyboardInterrupt:
            print("You have cancelled the program execution.")
            print("Exiting...")
            exit(1)
        
    # End while loop    


if __name__ == "__main__":
    main()