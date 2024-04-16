"""Class writing practice."""

class Profile:
    # Attributes
    username: str
    private: bool

    # Making the init constructor; basically just serves to define attributes.
    def __init__(self, username_input: str):
        """Create a new class Profile object."""
        self.username = username_input
        self.private = True

    
    def tweet(self, msg: str):
        """Prints a message if profile is public."""
        if self.private is False:  # could also say "if not self.private"
            print(msg)

    
# Instantiation
user1: Profile = Profile("110_rulez") # calls __init__
user1.private = False
user1.tweet("OOP is cool!")


