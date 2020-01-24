#
#
#
class Source:
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.posZ = 0

    def __init__(self, x, y, z):
        self.posX = x 
        self.posY = y 
        self.posZ = z

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