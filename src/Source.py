#
#
#
class Source:
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
        self.name = name
        self.location_name_10_20 = locationName
        
    def setName(self, name, locationName):
      	self.name = name
        self.location_name_10_20 = locationName
        
    def getName(self):
      	to_return = []
        to_return.append(self.name)
        to_return.append(self.location_name_10_20)
        return to_return

    def setPos(self, x, y, z):
        self.posX = x 
        self.posY = y 
        self.posZ = z 

    def getPos(self):
        toret = []
        toret.append(self.posX)
        toret.append(self.posY)
        toret.append(self.posZ)
        return toret