from car import Car

class Battery:
    """A simple class that models a battery."""

    def __init__(self, battery_size=40):
        """"Initialise a battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print the battery specification."""
        print(f"The car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Attributes of an Electric Car."""

    def __init__(self, make, model, year):
        """
        Initialise the attributes of the parent car.
        Then initialise attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
