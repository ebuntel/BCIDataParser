from Detector import Detector
from Source import Source

class RawDataChannel:
    """Holds the data of one channel (a channel is one source linked to one detector).
    Data on the source and detectors are retrieved from the probe info files using the retrieveSource and 
    retrieveDetector functions below.
    Instances of this class are contained in the RawData class.

    Attributes:
        source: Contains the source half of this channel object. Starts as none and is filled by the retrieveSource function.
        detector: Contains the detector half of this channel object. Starts as none and is filled by the retrieveDetector function.
        badDataFlag: A bool used to flag channels that contain bad data. Default is false.
        name: The name of the raw data channel. Takes the form C# (ex: C1, C13, C21, and so on).
    """

    # Constructors

    def __init__(self):
        self.source = None
        self.detector = None
        self.badDataFlag = False
        self.name = ""

    #

    # Getters and Setters

    def getSource(self):
        return self.source

    def getDetector(self):
        return self.detector

    def getDataFlag(self):
        return self.badDataFlag

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def setDataFlag(self, newFlag):
        self.badDataFlag = newFlag

    #

    def retrieveSource(self, sourceNum, probeInfo):
        """

        """
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

    def retrieveDetector(self, detectorNum, probeInfo):
        """

        """
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
