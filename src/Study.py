
class Study:
    """Data class that represents a Study object

    Attributes:
        name: Name of the Study object
    """

    def __init__(self):
        self.name = ""

    # Getters and Setters

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    #