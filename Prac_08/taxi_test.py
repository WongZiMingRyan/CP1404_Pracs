from Practical.Prac_08.taxi import Taxi


def main():
    """Demo test code to show how to use car class."""
    Prius_1 = Taxi("Prius 1", 100, 1.23)
    Prius_1.drive(40)
    print(Prius_1, Prius_1.get_fare())
    Prius_1.start_fare()
    Prius_1.drive(100)
    print(Prius_1, Prius_1.get_fare())


main()
