class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints name and cuisine type."""
        print(f"The restaurant {self.restaurant_name} is famous for {self.cuisine_type} food.")
    
    def open_restaurant(self):
        """Simulates the opening of a restaurant."""
        print(f"The restaurant {self.restaurant_name} is open.")

restaurant1 = Restaurant('Amar', 'South Indian')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('Spring Fields', 'Global Fusion')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('Avenue', 'North Indian')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()