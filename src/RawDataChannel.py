
class RawDataChannel:
    """Holds the data of one channel (a channel is one source linked to one detector).
    Data on the source and detectors are retrieved from the probe info files using the retrieveSource and
    retrieveDetector functions below.
    Instances of this class are contained in the RawData class.

    Attributes:
        source: The source number
        detector: the detector number
        badDataFlag: A bool used to flag channels that contain bad data. Default is false.
        name: The name of the raw data channel. Takes the form C# (ex: C1, C13, C21, and so on).
        wavelength: The wavelength of the channel.
    """

    # Constructors
    def __init__(self):
        self.source = 0
        self.detector = 0
        self.badDataFlag = False
        self.name = ""
        self.wavelength = 0
        self.key=0
        self.channel_num=0

    def retrieveWavelength(self, index, nirsFile):
        """Retrieves the wavelength of the channel

        Args:
            index: The index of the desired wavelength in the wavelength array
            nirsFile: The dictionay loadmat returns when the .nirs file is loaded

        Returns: 0 if successful, -1 if not
        """

        if(index == 0):
            self.wavelength = nirsFile['SD']['Lambda'][0][0][0][0]
            return 0
        elif(index == 1):
            self.wavelength = nirsFile['SD']['Lambda'][0][0][0][1]
            return 0
        else:
            return -1


    def printRDC(self):
        print("Raw Data Channel ", self.name)
        print("Source: ", self.source)
        print("Detector: ", self.detector)
        if self.badDataFlag:
            print("This channel contains bad data!")
