from Study import Study
from Subject import Subject

class DefinedStudyEvent:
    """Data class that holds both a Study object, and an Event object

    Attributes:
        name: Name of this DefinedStudyEvent object
        study: The Study object confined in this class
        sub: The Subject object confined in this class
    """

    def __init__(self):
        self.name = ""
        self.study = None
        self.sub = None

    # Getters and Setters

    def getName(self):
        return self.name

    def getStudy(self):
        return self.study

    def getSubject(self):
        return self.sub

    def setName(self, newName):
        self.name = newName

    def setStudy(self, study):
        self.study = study

    def setSubject(self, sub):
        self.sub = sub

    #