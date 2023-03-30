# import myexceptions as me
from myexceptions import OutOfRangeException, NegativeNetSalaryException, TooMuchNetSalaryException, NegativeChildrenException, TooManyChildrenException

MINIMUM_WAGE = 1200
COST_SCHOOL_CANTENN = 250
MAX_CHILDREN_SINGLE_PARENTAL = 5
MAX_CHILDREN_FAMILY = 3
MAX_SUBVENTION = 1000

def get_number(caption, min_value, max_value):

    valid_number = False

    while not valid_number:

        try:
            number = float(input(caption))
            if number < min_value or number > max_value:
                raise OutOfRangeException("Number out of range")

        except (ValueError, TypeError):
            print("The number entered is not valid. It included some character not allowed.")
            print("Try it again...")

        except KeyboardInterrupt:
            print("User requests to abort the program.")
            exit(1)
        
        except OutOfRangeException as oore:
            print(oore.__str__())
            print(f"The number must be between {min_value} and {max_value}")
            print("Try it again...")

        except:
            print("It has happened some exception.")
            print("Try it again...")

        else:
            valid_number = True

        finally:
            # Ending clause
            print("The final clause always is executed.")

    return number


def get_perc_subvention(net_salary):

    """
    Function:           get_perc_subvention
    Description:        It calculate the percentage subvention according to the apliccant's net salary .
    Parameters:
        net_salary:     The net salary
    Return:             The % of subvention.
    """

    try:
        if net_salary < 0:
            raise NegativeNetSalaryException("The net salary cannot be negative.")
        elif net_salary < MINIMUM_WAGE:
            perc = 0.8
        elif net_salary >= MINIMUM_WAGE and  net_salary < MINIMUM_WAGE * 2:
            perc = 0.5
        elif net_salary >= MINIMUM_WAGE * 2 and net_salary < MINIMUM_WAGE * 3:
            perc = 0.2
        else:
            raise TooMuchNetSalaryException(f"Your salary {net_salary} exceeds the maximun salary allowed.")

    except NegativeNetSalaryException as nnse:
        print(nnse.__str__())
        perc = 0

    except TooMuchNetSalaryException as tmnse:
        print(tmnse.__str__())
        perc = 0
    
    return perc


def get_total_subvention(children, percentage_subvention, single_parent):

    """
    Function:                   get_total_subvention
    Description:                It calculate the subvention granteed to and applicant for the school canteer.
    Parameters:
        children:               The number of children the subvention is requested for.
        percentage_subvention:  % of subvention granted.
        single_parent:          Boolean to point out if the family is single parent.
    Return:                     The total subvention granted.
    """

    subvention_per_child = COST_SCHOOL_CANTENN * percentage_subvention

    try:
        if children < 0:
            raise NegativeChildrenException("The number of children cannot be negative")

        if children > MAX_CHILDREN_SINGLE_PARENTAL and single_parent:
            raise TooManyChildrenException(f"The number of children exceeds the maximum of {MAX_CHILDREN_SINGLE_PARENTAL}")

        if children > MAX_CHILDREN_FAMILY and not single_parent:
            raise TooManyChildrenException(f"The number of children exceeds the maximum of {MAX_CHILDREN_FAMILY}")
        
        total_subvention = subvention_per_child * children

    except NegativeChildrenException as nce:
        print(nce.__str__())
        total_subvention = 0

    except TooManyChildrenException as tmce:
        print(tmce.__str__())
        if single_parent:
            total_subvention = subvention_per_child * MAX_CHILDREN_SINGLE_PARENTAL
        else:
            total_subvention = subvention_per_child * MAX_CHILDREN_FAMILY

    finally:
        if total_subvention > MAX_SUBVENTION:
            total_subvention = MAX_SUBVENTION
    
    return total_subvention