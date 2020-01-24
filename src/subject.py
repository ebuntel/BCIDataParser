from Detector import Detector
from Source import Source

#
#
#
class Subject:

    def __init__(self):
        self.detectors = []
        self.sources = []

    def getDetectors(self, fileDict):
        for det in fileDict['SD']['DetPos'][0][0]:
            newDet = Detector(det[0], det[1], det[2])
            self.detectors.append(newDet)
        return 0

    def getSources(self, fileDict):
        for src in fileDict['SD']['SrcPos'][0][0]:
            newSrc = Source(src[0], src[1], src[2])
            self.sources.append(newSrc)
        return 0

    def printDetectors(self):
        for det in self.detectors:
            print(det.getPos())
        return 0

    def printSources(self):
        for src in self.sources:
            print(src.getPos())
        return 0
