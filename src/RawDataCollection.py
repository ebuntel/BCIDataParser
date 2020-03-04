from RawDataChannel import RawDataChannel
from Detector import Detector
from Source import Source
from RawData import RawData
from DeviceSetup import DeviceSetup

class RawDataCollection:
    """A top-level data class for holding the RawData, RawDataChannel, Source, and Detector objects

    Attributes:
        channels: Contains all of the channels (There are 42 channels, 21x2 wavelengths)
        sources: Contains all of the sources (There are 8 sources)
        detectors: Contains all of the detectors (There are 8 detectors)
    """

    def __init__(self):
        self.channels = []
        self.sources = []
        self.detectors = []
        self.raw_data_list = []
        self.device_setup= DeviceSetup()

    def retrieveRawData(self, nirsFile):
        """Retrieves all of the data points from the fNIRS file.

        Args:
            nirsFile: The dictionary returned by loadmat when loading the .nirs file

        Returns:
            Nothing
        """
        time_series=nirsFile['t']
        # first 21 cols is data at 760, other 21 cols is 850


        rows= len(nirsFile['d'])
        cols = len(nirsFile['d'][0])
        # print(nirsFile['t'][1], type(nirsFile['t'][1]))
        # print(nirsFile['t'][1][0], type(nirsFile['t'][1][0]))
        # print(nirsFile['t'], type(nirsFile['t']))

        print(cols)
        # format nirsFile['d'][row] return all values in row

        print(nirsFile['d'][0][1])
        for r in range(rows):
            # temporarily hard code channel number
            # print(nirsFile['d'][r])
            for c in range(21):
                new_data= RawData()
                new_data.time = nirsFile['t'][r][0]
                new_data.channel=c+1
                new_data.value=nirsFile['d'][r][c]
                new_data.wavelength=760
                self.raw_data_list.append(new_data)
                # print(r, new_data.channel, new_data.value)
                # s=input()


        for r in range(rows):
            # temporarily hard code channel number
            col=1
            for c in range(21, cols):
                new_data= RawData()
                new_data.time = nirsFile['t'][r][0]
                new_data.channel=col
                new_data.value=nirsFile['d'][r][c]
                new_data.wavelength=850
                # print(r,new_data.channel, new_data.value)
                self.raw_data_list.append(new_data)
                col+=1
                # s=input()

        # rowNum = 0
        # for row in nirsFile['d']:
        #     colNum = 0
        #     for col in nirsFile['d'][rowNum]:
        #         time = nirsFile['t'][rowNum][0]
        #         temp = RawData(time, col, colNum+1)
        #         self.raw_data_list.append(temp)
        #         colNum += 1
        #     rowNum += 1

    def retrieveRawDataChannels(self, probeInfo, nirsFile):
        """Creates channel objects after first retrieving data from all of the sources and detectors

        Args:
            probeInfo: The dictionary returned by loadmat when loading the probeinfo file

        Returns:
            Nothing
        """
        cnt = 0
        # Channels with first wavelength
        for channelRow in probeInfo['probeInfo'][0][0]['probes']['index_c'][0][0]:
            channel = RawDataChannel()
            cnt += 1
            channel.retrieveWavelength(0, nirsFile)
            name = "C" + str(cnt) + "," + str(channel.wavelength)
            channel.source=(int(channelRow[0]))
            channel.detector=(int(channelRow[1]))
            channel.name=(name)
            channel.channel_num=cnt
            self.channels.append(channel)

        cnt = 0
        # Channels with second wavelength
        for channelRow in probeInfo['probeInfo'][0][0]['probes']['index_c'][0][0]:
            channel = RawDataChannel()
            cnt += 1
            channel.retrieveWavelength(1, nirsFile)
            name = "C" + str(cnt) + "," + str(channel.wavelength)
            channel.source=(int(channelRow[0]))
            channel.detector=(int(channelRow[1]))
            channel.name=(name)
            channel.channel_num=cnt
            self.channels.append(channel)

    def retrieveSourcesAndDetectors(self, probeInfo):
        """Retrieves the data for all of the sources and detectors from the probeinfo file

        Args:
            probeInfo: The dictionary loadmat returns when the probeinfo file is loaded

        Returns:
            0 if successful, -1 if not
        """
        src_dir_num = int(probeInfo['probeInfo'][0][0]['probes']['nSource0'][0][0][0][0])
        for num in range(0, src_dir_num):
            temp_src = self.retrieveSource(num, probeInfo)
            if(temp_src != None):
                self.sources.append(temp_src)
            else:
                return -1
            temp_dir = self.retrieveDetector(num, probeInfo)
            if(temp_dir != None):
                self.detectors.append(temp_dir)
            else:
                return -1
        return 0


    def retrieveSource(self, sourceNum, probeInfo):
        """Retrieves source data for the given source from the probeinfo file

        Args:
            sourceNum: The number of the source to retrieve data for (1 to 8)
            probeInfo: The dictionary loadmat returns when the probeinfo file is loaded

        Returns:
            A new source if successful, None if not
        """

        try:
            name = str(sourceNum+1)
            locationName = probeInfo['probeInfo'][0][0]['probes']['labels_s'][0][0][0][sourceNum][0]
            xCoord = probeInfo['probeInfo'][0][0]['probes']['coords_s3'][0][0][sourceNum][0]
            yCoord = probeInfo['probeInfo'][0][0]['probes']['coords_s3'][0][0][sourceNum][1]
            zCoord = probeInfo['probeInfo'][0][0]['probes']['coords_s3'][0][0][sourceNum][2]
            return Source(xCoord, yCoord, zCoord, name, locationName)
        except KeyError:
            print("Source parsing failed")
            return None

    def retrieveDetector(self, detectorNum, probeInfo):
        """Retrieves detector data for the given source from the probeinfo file

        Args:
            detectorNum: The number of the detector to retrieve data for (1 to 8)
            probeInfo: The dictionary loadmat returns when the probeinfo file is loaded

        Returns:
            A new detector if successful, None if not
        """

        try:
            name = str(detectorNum+1)
            locationName = probeInfo['probeInfo'][0][0]['probes']['labels_d'][0][0][0][detectorNum][0]
            xCoord = probeInfo['probeInfo'][0][0]['probes']['coords_d3'][0][0][detectorNum][0]
            yCoord = probeInfo['probeInfo'][0][0]['probes']['coords_d3'][0][0][detectorNum][1]
            zCoord = probeInfo['probeInfo'][0][0]['probes']['coords_d3'][0][0][detectorNum][2]
            return Detector(xCoord, yCoord, zCoord, name, locationName)
        except KeyError:
            print("Detector parsing failed")
            return None
