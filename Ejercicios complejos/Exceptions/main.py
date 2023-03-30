"""
Project:        Exception
Author:         Alberto Sánchez Barona
Date:           07/11/2022
Formulation:
                Develop a program to calculate the subventions for school canteens (comedor escolar).
                It must enter by keyboard:
                    - Applicant's name -> 
                    - Net Salary -> 
                    - Name of children -> 
                    - If it is single-parental family -> 
                
                The cost of school canteen is 250 € a month per child.
                Conditions:
                    - Subventions is only for people that earn until free time the minimun wage (1200€ a month).
                    - Subvention granted is according the next table:
                        Salary                          Subvention
                        ------------------------------------------
                        < MW                            80% school canteen cost
                        1 MW - 2 MW                     50%
                        2 MW - 3 MW                     20%

                    - The subvention is for each child with a maximun of 5 in single parental families, 3 otherwise.
                    - The maximun subvention is 1000 € for all childrens.
"""

import functions as f
import generic_functions as gf
from myexceptions import NegativeChildrenException, TooManyChildrenException


def main():

    enter_data = True

    while enter_data:

        applicant_name = input("Enter your name: ")

        net_salary = f.get_number("Enter your net salary: ", 0, f.MINIMUM_WAGE * 3)

        children = int(f.get_number("Enter the number of children registered at school: ", 1, 5))

        single_parent = gf.question_yes_no("Is your family single-parental")

        percentage_subvention = f.get_perc_subvention(net_salary)

        total_subvention = f.get_total_subvention(children, percentage_subvention, single_parent)
        
        print(f"Your name is {applicant_name}, your salary is {net_salary}")
        print(f"You have {children} children.")
        print("Is your family single-parental?", single_parent)
        print(f"Your subvention % is {percentage_subvention}")
        print(f"Your subvention is {total_subvention}")


if __name__ == "__main__":
    main()