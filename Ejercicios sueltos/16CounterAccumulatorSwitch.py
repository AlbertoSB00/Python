"""

Program: 16CounterAccumulatorSwitch.py
Author: Alberto Sánchez Barona
Date: 14/10/2022
Description: Example of use of counter, accumulator and switches.

"""

# There are 3 types of special variables according to a specific use:
# Counter -> Integer variable. It counts how many times an event has happened.
# Accumulator -> Integer variable. It accumulates or adds different amount of something.
# Switch -> Boolean integer. It warns if an event has happened or not.

# Develop a program that enters by keyboard marks of several pupils in a subject until the mark is negative.
# Display in the screen how many of them are passed and how many are failed.
# 2nd part: Calculate the average mark for the passed pupils and for the failed ones.

passed = 0
failed = 0

avg_passed = 0
avg_failed = 0

while True:
    mark = float(input("Enter a mark (negative to leave): "))
    if mark < 0:
        break
    if mark >= 5 and mark <= 10:
        passed += 1
        avg_passed += mark
    if mark >= 0 and mark < 5:
        failed += 1
        avg_failed += mark

    if mark > 10:
        print("Error. The mark must be between 0 and 10.")

print(f"{passed} pupils have passed and {failed} one have failed.")

if passed > 0:
    avg_passed /= passed
    print(f"The average mark for passed pupils is {avg_passed}")
else:
    print("There iare not passed pupils.")

if failed > 0:
    avg_failed /= passed
    print(f"The average mark for failed pupils is {avg_failed}")
else:
    print("There are not failed pupils.")