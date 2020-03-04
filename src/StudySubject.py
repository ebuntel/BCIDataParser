from Study import Study
from Subject import Subject

class StudySubject:
    """A data class that holds both a Subject object, and a Study object

    Attributes:
        study: Study object contained in this StudySubject object
        sub: Subject object contained in this StudySubject object
        name: Name of this StudySubject object
    """

    def __init__(self):
        self.study = None
        self.sub = None
        self.name = ""

    # Getters and Setters

    def getStudy(self):
        return self.study

    def getSubject(self):
        return self.sub

    def getName(self):
        return self.name

    def setStudy(self, study):
        self.study = study

    def setSubject(self, sub):
        self.sub = sub

    def setName(self, newName):
        self.name = newName

    #