def get_category() -> str:

    valid_category = False

    while not valid_category:

        category = input("Enter the partner's category: ")

        if category == "COP" or category == "TEC" or category == "ACT":
            valid_category = True
        else:
            print(f"ERROR -> The category {category} is not valid.")
            print(f"Please, enter COP, TEC or ACT")

    return category
# End of the function get_category()


def get_base_quota(category: str) -> int:

    valid_quota = False

    match category:
        case "COP":
            min_value = 60
            max_value = 120
        case "TEC":
            min_value = 40
            max_value = 59
        case "ACT":
            min_value = 20
            max_value = 30
        case _:
            base_quota = 0
            valid_quota = True

    # End of match statement.

    while not valid_quota:

        base_quota = int(input("Enter your base quota: "))

        if base_quota >= min_value and base_quota <= max_value:
            valid_quota = True
        else:
            print("ERROR -> The base quota is not valid.")
            print(f"It must be between {min_value}€ and {max_value}€")
            print("Try it again...")

    # End of while loop.

    return base_quota

# End of the function get_base_quota()

def get_age():

    valid_age = False

    while not valid_age:

        age = int(input("Enter the number of months you are member: "))

        if age > 0:
            valid_age = True
        else:
            print("ERROR -> The age is not valid, it cannot be a negative number.")
            print("Try it again...")

    # End of while loop.

    return age

# End of the function get_age()

def get_total_discount(category: str, years_age: int, months_age: int) -> float:

    total_discount = 0

    match category:
        case "COP":
            total_discount = years_age * 0.5 + months_age * (0.5 / 12)
        case "TEC":
            total_discount = years_age * 1 + months_age * (1 / 12)
        case "ACT":
            total_discount = years_age * 2 + months_age * (2 / 12)
        case _:
            total_discount = 0

    # End of match statement

    if total_discount > 5:
        total_discount = 5

    return total_discount

# End of the function get_total_discount()