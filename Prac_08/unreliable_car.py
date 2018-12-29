from Practical.Prac_08.car import Car
import random


class Unreliable_Car(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(fuel, name)
        self.reliability = reliability
        self.current_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}".format(super().__str__())

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        drive_chance = random.randint(0, 100)
        if drive_chance > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        self.current_distance += distance_driven
        return distance_driven

