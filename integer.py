#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 10.13.22
# This program checks if the user given integer is positive or negative
# or 0.


# This function checks if the integer is equal, greater or less than 0.
def main():
    user_integer = int(input("What is your integer?: "))
    # If the user integer is 0 the output will say so.
    if user_integer == 0:
        print("{} is just 0".format(user_integer))
    # If the user input is greater than 0 it is positive.
    elif user_integer > 0:
        print("{} is positive.".format(user_integer))
    # In any other scenario the outcome is the integer is negative
    else:
        print("{} is negative.".format(user_integer))


# This checks runs our program.
if __name__ == "__main__":
    main()
