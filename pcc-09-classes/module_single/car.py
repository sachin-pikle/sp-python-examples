"""A module with a set of classes that can be used to represent electric and gas cars."""

class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialise the car's attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_car(self):
        """Print the long name of the car."""
        description = f"{self.year} {self.make} {self.model}"
        return description.title()

    def read_odometer(self):
        """Print the car's mileage."""
        print(f"The car has {self.odometer_reading} miles on it.")


    def update_odometer(self, new_mileage):
        """Update the car's mileage."""
        if new_mileage > self.odometer_reading:
            self.odometer_reading = new_mileage
        else:
            print(f"Cannot reset odometer.")


    def increment_odometer(self, increment):
        """Increment the car's mileage."""
        if increment >= 0:
            self.odometer_reading += increment
        else:
            print(f"Cannot decrement the mileage.")

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
