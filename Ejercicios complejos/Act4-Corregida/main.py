"""
Program:        main.py
Author:         Alberto Sánchez Barona
Date:           04/11/2022
Description:

"""

import module as m
import generic_functions as gf

total_quotas = 0
count_partners = 0

while True:
    partner_name = input("Enter your name: ")
    if partner_name == "":
        break

    # We get the partner's category.
    category = m.get_category()

    # We get the initial quota for the partner.
    base_quota = m.get_base_quota(category)
    print(f"The base quota is: {base_quota}")

    # We get the partner's age.
    age = m.get_age()

    # We split the age in years and months
    years_age = age // 12
    months_age = age % 12
    print(f"Your age is {years_age} years and {months_age} months.")

    # We check if the partner wants to sponsor children.
    if gf.question_yes_no("Do you want to sponsor children"):
        perc_sponsor_children = 0.1
        if category == "COP":
            perc_sponsor_children = 0.125
    else:
        perc_sponsor_children = 0

    # We check if the partner want to contribute in solidarity campaign.
    if gf.question_yes_no("Do you want to contribute to our solidarity campaign"):
        perc_solidarity_campaign = 0.05
        if category == "COP":
            perc_solidarity_campaign = 0.075
    else:
        perc_solidarity_campaign = 0

    print(f"% for sponsor children {perc_sponsor_children}")
    print(f"% for solidarity campaign {perc_solidarity_campaign}")

    # Discount for age
    total_discount = m.get_total_discount(category, years_age, months_age)
    print("Your discount is", total_discount)

    # Calculations for the partner's quota
    initial_quota = base_quota - total_discount
    print("Your initial quota is", initial_quota)

    # Increasing for children sponsor
    plus_children_sponsor = initial_quota * perc_sponsor_children
    print("Your increasing for children sponsor is", plus_children_sponsor)

    # Increasing for solidarity campaign
    plus_solidarity_campaign = initial_quota * perc_solidarity_campaign
    print("Your increasing for solidarity campaign is", plus_solidarity_campaign)

    # Net quota
    net_quota = initial_quota + plus_children_sponsor + plus_solidarity_campaign
    print(f"Your final quota is {net_quota}")

    # We count one partner more and add the quota
    count_partners += 1
    total_quotas += net_quota

# End while loop.
print(f"We have {count_partners} partners with {total_quotas} as total quotas.")
print("Exiting...")
exit(0)