"""

Program: 06AssignmentOperators.py
Author: Alberto Sánchez Barona
Date: 28/09/2022
Description: Using the assignment operators. There area other assignment operators beside the =. They involved and
             operation and then, and assignment to a variable. They could only be used with variables, if could we used
             literal in one operand thought.
             += Addition and assignment
             -=
             *=
             /=
             //=
             %=
             **=

"""

# += Operator
integer_number = 4
another_number = 6
# This is equivalent to integer_number = integer_number +5
integer_number += 5
print("Now, integer_number is", integer_number)
integer_number += another_number
print("Now, integer_number is", integer_number)
integer_number += another_number * 2
print("Now, integer_number is", integer_number)

# -= Operator
integer_number -= 7
print("Now, integer_number is", integer_number)

# *= Operator
integer_number *= 2
print("Now, integer_number is", integer_number)

# /= Operator
integer_number /= 10
print("Now, integer_number is", integer_number)