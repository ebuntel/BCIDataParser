import numpy as np

from scipy.io import loadmat
from RawDataChannel import RawDataChannel

#
#
#

# def testSourceAndDetectorPrints():
#     src = Source(1.0, 2.0, -4.5, "george", "feckoff")
#     det = Detector(-1100, 7.8, 4, "Arnold", "det feckoff")
#     src.printSource()
#     det.printDetector()

def main():
  data = loadmat("223_AXCPT19_CH_probeinfo.mat")

  channelList = []

  for channelRow in data['probeInfo'][0][0]['probes']['index_c'][0][0]:
    channel = RawDataChannel()
    channel.getSource(int(channelRow[0]), data)
    channel.getDetector(int(channelRow[1]), data)
    channelList.append(channel)
  
  for channel in channelList:
    channel.printRDC()

if __name__ == "__main__":
    main()



