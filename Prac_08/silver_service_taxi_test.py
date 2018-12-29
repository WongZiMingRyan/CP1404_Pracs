from Practical.Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Demo test code to show how to use car class."""
    Prius_1 = SilverServiceTaxi("Prius 1", 100, 1.23, 3)
    Prius_1.drive(40)
    print(Prius_1)
    Prius_1.start_fare()
    Prius_1.drive(100)
    print(Prius_1)


main()
