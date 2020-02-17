
class Sensor:
    """Data class that holds data for a Sensor object

    Attributes:
        name: The name of this Sensor object
    """

    def __init__(self):
        self.name = ""

    # Getters and Setters

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    #