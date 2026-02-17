class User:
    """A simple attempt to model a user profile."""

    def __init__(self, first_name, last_name):
        """Initialise the user's first name and last name."""
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        """Prints the user's first name and last name."""
        print(f"User's full name is {self.first_name} {self.last_name}.")
    
    def greet_user(self):
        """Greet the user."""
        print(f"Welcome back, {self.first_name}!")

user1 = User("Minnie", "Mouse")
user1.describe_user()
user1.greet_user()

user2 = User("Mickey", "Mouse")
user2.describe_user()
user2.greet_user()