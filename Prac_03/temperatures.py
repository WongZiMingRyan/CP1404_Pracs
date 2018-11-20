"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    def C_to_F():
        global celsius, fahrenheit
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))

    def F_to_C():
        global fahrenheit, celsius
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))

    while choice != "Q":
        if choice == "C":
            C_to_F()
        elif choice == "F":
            F_to_C()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
