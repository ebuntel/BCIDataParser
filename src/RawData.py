from RawDataChannel import RawDataChannel

class RawData:
    """
    """

    # Constructors

    def __init__(self):
        self.channels = []

    #

    # Getters and Setters

    #

    def retrieveRawDataChannels(self, probeInfo):
        """
        """
        for channelRow in probeInfo['probeInfo'][0][0]['probes']['index_c'][0][0]:
            channel = RawDataChannel()
            channel.retrieveSource(int(channelRow[0]), probeInfo)
            channel.retrieveDetector(int(channelRow[1]), probeInfo)
            self.channels.append(channel)