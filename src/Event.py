
class Event:
    """Data class that represents an Event object

    Attributes:
        name: Name of this event
        long_desc: Description of this event
    """

    def __init__(self):
        self.name = ""
        self.long_desc = ""

    # Getters and Setters

    def getName(self):
        return self.name

    def getLongDesc(self):
        return self.long_desc

    def setName(self, newName):
        self.name = newName

    def setLongDesc(self, desc):
        self.long_desc = desc

    #