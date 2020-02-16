from RawDataChannel import RawDataChannel

class RawData:
    """Top-level class for holding the data parsed from the nirs and probeinfo files

    Attributes:
        channels: A list of all of the channels involved in this experiment.  
    """

    # Constructors

    def __init__(self):
        self.channels = []

    #

    # Getters and Setters

    def getChannels(self):
        return self.channels

    #

    def retrieveRawDataChannels(self, probeInfo):
        """
        """
        cnt = 0
        for channelRow in probeInfo['probeInfo'][0][0]['probes']['index_c'][0][0]:
            cnt += 1
            name = "C" + str(cnt)
            channel = RawDataChannel()
            channel.retrieveSource(int(channelRow[0]), probeInfo)
            channel.retrieveDetector(int(channelRow[1]), probeInfo)
            channel.setName(name)
            self.channels.append(channel)