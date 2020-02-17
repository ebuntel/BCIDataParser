from Study import Study
from Sensor import Sensor

class DefinedStudySensor:
    """Data class that contains both a Sensor object, and a Study object

    Attributes:
        name: Name of this DefinedStudySensor object
        study: Study object contained in this class
        sensor: Sensor object contained in this class
    """

    def __init__(self):
        self.name = ""
        self.study = None
        self.sensor = None

    # Getters and Setters

    def getName(self):
        return self.name

    def getStudy(self):
        return self.study

    def getSensor(self):
        return self.Sensor

    def setName(self, newName):
        self.name = newName

    def setStudy(self, study):
        self.study = study

    def setSensor(self, sensor):
        self.sensor = sensor

    #