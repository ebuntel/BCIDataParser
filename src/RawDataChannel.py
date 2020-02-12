from Detector import Detector
from Source import Source

#
#
#
class RawDataChannel:

    def __init__(self):
        self.source = None
        self.detector = None
        self.badDataFlag = False
        self.name = ""

    def getSource(self, sourceNum, probeInfo):
        sourceNum -= 1

        try:
            name = str(sourceNum+1)
            locationName = probeInfo['probeInfo'][0][0]['probes']['labels_s'][0][0][0][sourceNum][0]
            xCoord = probeInfo['probeInfo'][0][0]['probes']['coords_s3'][0][0][sourceNum][0]
            yCoord = probeInfo['probeInfo'][0][0]['probes']['coords_s3'][0][0][sourceNum][1]
            zCoord = probeInfo['probeInfo'][0][0]['probes']['coords_s3'][0][0][sourceNum][2]
            self.source = Source(xCoord, yCoord, zCoord, name, locationName)
        except KeyError:
            print("Source parsing failed")
        

    def getDetector(self, detectorNum, probeInfo):
        detectorNum -= 1

        try:
            name = str(detectorNum+1)
            locationName = probeInfo['probeInfo'][0][0]['probes']['labels_d'][0][0][0][detectorNum][0]
            xCoord = probeInfo['probeInfo'][0][0]['probes']['coords_d3'][0][0][detectorNum][0]
            yCoord = probeInfo['probeInfo'][0][0]['probes']['coords_d3'][0][0][detectorNum][1]
            zCoord = probeInfo['probeInfo'][0][0]['probes']['coords_d3'][0][0][detectorNum][2]
            self.detector = Detector(xCoord, yCoord, zCoord, name, locationName)
        except KeyError:
            print("Detector parsing failed")

    def printRDC(self):
        print("Raw Data Channel ", self.name)
        if self.source != None:
            self.source.printSource()
        if self.detector != None:
            self.detector.printDetector()
        if self.badDataFlag:
            print("This channel contains bad data!")
