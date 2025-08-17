class Dog:
    """
    A class to represent a dog.
    """

  
    species = "Canis familiaris"

    def __init__(self, name, breed):
        """
        Initialize name and breed.
        """
        self.name = name
        self.breed = breed

    def describe(self):
        """
        Return a description string.
        """
        return f"{self.name} is a {self.breed}. Species: {self.species}."



dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")


print(dog1.describe())
print(dog2.describe())


dog1.species = "Canis lupus"


print("\nAfter modifying dog1's species:")
print(dog1.describe())  
print(dog2.describe())  
