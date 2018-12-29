from Practical.Prac_08.taxi import Taxi
flagfall = 4.50


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, price_per_km, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel, price_per_km)
        self.price_per_km = price_per_km * fanciness
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""

        return "{} plus flagfall of ${:.2f}".format(super().__str__(), flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance + flagfall

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

