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