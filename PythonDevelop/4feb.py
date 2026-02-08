class Athelete:
    """
    A class to represent an athlete."""
    def __init__(self, name):
        self.name = name
        """
        Initialize the athlete with a name.
        """

    #def display(self):
    #    """
    #    Display the athlete's name."""
    #   print(f"Athlete Name: {self.name}")

    def __str__(self):
        """
        Is used to provide a humman-reader string representation of the object.
        It is intended to be used bt end-users and should be concise and easy to understand."""
        return f"Athlete is: ({self.name})"
    
    def __repr__(self):
        """
        Is used to provide an unambiguous string representation of the object.
        It is intended to be used by developers and should include more detailed information."""
        return f"Athelete(name='{self.name}')"

# Example usage
if __name__ == "__main__":
    a = Athelete("Usain Bolt")
    b = Athelete("Emmanuel Gallegos")
    c = Athelete("Emiliano Robledo")
    print(f"{a} & {b} & {c}")

    g = eval(repr(a))
    print(type(g))

