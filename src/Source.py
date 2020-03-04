
class Source:
    """Holds the information for one source.

    Attributes:
        posX: The x position of the source (From the coords_s3 subsection of the probeinfo file)
        posY: The y position of the source (From the coords_s3 subsection of the probeinfo file)
        posZ: The z position of the source (From the coords_s3 subsection of the probeinfo file)
        name: The source's number
        location_name_10_20: The detector's 10-20 location (From the labels_s subsection of the probeinfo file)
    """

    # Constructors

    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.posZ = 0
        self.name = ""
        self.location_name_10_20 = ""

    def __init__(self, x, y, z, name, locationName):
        self.posX = x
        self.posY = y
        self.posZ = z
        self.name = "S"+ name
        self.location_name_10_20 = locationName
        self.key=0

    #

    # Getters and Setters

    def setName(self, name, locationName):
        self.name = name
        self.location_name_10_20 = locationName

    def setPos(self, x, y, z):
        self.posX = x
        self.posY = y
        self.posZ = z

    def getName(self):
        to_return = []
        to_return.append(self.name)
        to_return.append(self.location_name_10_20)
        return to_return

    def getPos(self):
        toret = []
        toret.append(self.posX)
        toret.append(self.posY)
        toret.append(self.posZ)
        return toret

    #

    def printSource(self):
        print("Source ", self.name)
        print("XPos: ", self.posX)
        print("YPos: ", self.posY)
        print("ZPos: ", self.posZ)
        print("Location name: ", self.location_name_10_20)
