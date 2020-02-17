
class Subject:
    """Holds the data for one subject.

    Attributes:
        bad_data_flag: Bool that indicates whether the subject's data is bad or not (default: false)
        name: Name of the subject
    """

    def __init__(self):
        self.bad_data_flag = False
        self.name = ""

    # Getters and Setters

    def getDataFlag(self):
        return self.bad_data_flag

    def getName(self):
        return self.name

    def setDataFlag(self, flag):
        self.bad_data_flag = flag

    def setName(self, newName):
        self.name = newName

    #