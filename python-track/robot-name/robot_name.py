import string
import random

# Cache unique robot names
cache = set()

class Robot:
    def __init__(self):
        # Initialize with an empty name
        self.name = None
        # Generate a random name during the first instantiation
        self.reset()
        
        
    def reset(self):
        """Reset the robot's name to a new random name, that hasn't been used previously."""
        while (name := self.__generate_random_name()) in cache:
            pass
        cache.add(name)
        self.name = name
        
        
    def __generate_random_name(self):
        """Generate a random name in the format of two uppercase letters followed by three digits."""
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        return "".join(letters + digits)
        
