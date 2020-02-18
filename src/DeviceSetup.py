
class DeviceSetup:
    """Data class holding various information on the device setup

    Attributes:
        name: Name of this DeviceSetup object
        update_rate_HZ: The frequency of fNIRS device
    """

    def __init__(self):
        self.name = ""
        self.update_rate_HZ = 0

    # Getters and Setters

    def getName(self):
        return self.name

    def getUpdateRate(self):
        return self.update_rate_HZ

    def setName(self, newName):
        self.name = newName

    def setUpdateRate(self, rate):
        self.update_rate_HZ = rate

    #
