"""

Program: E31.py
Author: Alberto Sánchez Barona
Date: 03/10/2022
Description: Develop a program that enters by keyboard a character called color in loop. The program finishes when the
             character is "f". For each character entered it has to display a message on the screen depending on
             its value:
                • Red, if color is "r" or "R".
                • Green, if color es "v" or "V".
                • Blue, if color is “a” or “A”.
                • Black, if color is any other character.

"""

color = ""
while color != "f":
    print("\tColor Menu")
    print("\t----------")
    print("Red color: r or R")
    print("Green color: g or G")
    print("Blue color: b or B")
    print("Black color: any character")
    print("E X I T: f")
    color = input("Select a color: ")
    match color:
        case "r" | "R":
            print("You selected red color.")
        case "g" | "G":
            print("You selected green color.")
        case "b" | "B":
            print("You selected blue color.")
        case "f":
            print("E X I T")
        case _:
            print("You selected black color.")
    input("Press enter to continue.")