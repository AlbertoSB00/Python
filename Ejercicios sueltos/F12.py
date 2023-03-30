"""

Program:        F12.py
Author:         Alberto Sánchez Barona
Date:           21/10/2022
Description:    Develop a function that receives as parameter a number that represents one mark between 0 and 10. It
                must return the grade related to the mark. Think about a way to manage no valid marks.

"""


def mark_grade(mark):
    match mark:
        case 0 | 1 | 2 | 3 | 4:
            result = "Your failed"
        case 5:
            result = "Your grade is C"
        case 6:
            result = "Your grade is B-"
        case 7 | 8:
            result = "Your grade is B"
        case 9:
            result = "Your grade is A"
        case 10:
            result = "Your grade is S"
        case _:
            result = "Your mark is wrong."
    return result


your_mark = int(input("Enter your mark: "))
result = mark_grade(your_mark)
print(result)