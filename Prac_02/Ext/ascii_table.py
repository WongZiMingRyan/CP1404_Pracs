MENU = """Enter a character for its ASCII value.
Enter a number between 33 and 127 for its character.
Enter 'ALL' for ALL characters and their ASCII values
Enter XX to quit
"""
LOWER = 33
UPPER = 127
while True:
    print(MENU)
    selection = input(">>>")
    if selection == "XX" or selection == "xx":
        print("See you next time")
        break
    if len(selection) == 1:
        print("The ASCII code for {} is {}".format(selection, ord(selection)))
    if selection.isdigit():
        if int(selection) < LOWER or int(selection) > UPPER:
            print("invalid input detected")
        else:
            print("the character for {} is {:>5}".format(selection, chr(int(selection))))
    if selection == "ALL" or selection == "All" or selection == "all":
        columns = input("How many columns would you like it to be printed in?")
        if columns.isdigit():
            print("Invalid input detected, please try again")
        print("{:>5} {:>5}".format("ASCII", "Char."))
        for i in range(LOWER, UPPER+1):
            print("{:>5} {:>5}".format(i, chr(i)))

    else:
        print("Invalid input detected")


