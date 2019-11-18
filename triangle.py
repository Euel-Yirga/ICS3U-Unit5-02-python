#!/usr/bin/env python3

# Created by: Euel Yirga
# Created on: Nov 2019
# This program uses user defined functions


def calculate_area(base, height):
    # calculate area

    # process
    area = base * height / 2 

    # output
    print("The area is {0} cm²".format(area))

def main():
    # this function gets length and width

    # input
    base_from_user = int(input("Enter the base of a triangle (cm): "))
    height_from_user = int(input("Enter the height of a triangle (cm): "))
    print("")

    #call functions
    calculate_area(base_from_user, height_from_user)

if __name__ == "__main__":
    main()
