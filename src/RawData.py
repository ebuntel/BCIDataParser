from RawDataChannel import RawDataChannel
from DeviceSetup import DeviceSetup
from Subject import Subject

class RawData:
    """Class for holding one data point containing info from the .nirs file and the probeinfo file

    Attributes:
        time_s: The time associated with this data point
        value: value of this data point
        time_source: Hard-coded value for time source
        bad_data_flag: Flag used to represent whether the data is bad or not (Default is False)
        device: DeviceSetup object associated with this data point
        channel: Channel associated with this object
    """

    # Constructors

    def __init__(self):
        self.time_s = 0.0
        self.value = 0.0
        self.time_source = "NIRSLAB_NIRS_SEC" #Currently hard-coded
        self.bad_data_flag = False
        self.device = None
        self.channel = 0

    def __init__(self, time, val, channel):
        self.time_s = time
        self.value = val
        self.time_source = "NIRSLAB_NIRS_SEC" #Currently hard-coded
        self.bad_data_flag = False
        self.device = None
        self.channel = channel

    #

    # Getters and Setters

    def getTime(self):
        return self.time_s

    def getVal(self):
        return self.value

    def getTimeSource(self):
        return self.time_source

    def getDataFlag(self):
        return self.bad_data_flag
    
    def getDeviceSetup(self):
        return self.device

    def getChannel(self):
        return self.channel

    def setDataFlag(self, flag):
        self.bad_data_flag = flag
    
    #

    def printDataPoint(self):
        toPrint = "t: " + str(self.time_s) + ", v: " + str(self.value)
        print(toPrint)
    