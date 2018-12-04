"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "azure1": "#f0ffff", "CadetBlue": "	#5f9ea0", "Coral": "#ff7f50", "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400", "DarkOrange": "#ff8c00", "DarkSalmon": "#e9967a", "GhostWhite": "	#f8f8ff"}
COLOR_UPPER = [color.upper() for color in COLOR_NAMES.keys()]
# print(STATE_NAMES)

color = input("Enter color name: ")
color = color.upper()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    if color == "ALL":
        for color in COLOR_NAMES:
            print("{0:<15} is {1}".format(color, COLOR_NAMES[color]))
    else:
        print("Invalid color name")
    state = input("Enter short name: ")
    state = state.upper()