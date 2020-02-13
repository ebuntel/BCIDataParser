import numpy as np

from scipy.io import loadmat
from RawData import RawData

# def testSourceAndDetectorPrints():
#     src = Source(1.0, 2.0, -4.5, "george", "feckoff")
#     det = Detector(-1100, 7.8, 4, "Arnold", "det feckoff")
#     src.printSource()
#     det.printDetector()

def main():
  data = loadmat("223_AXCPT19_CH_probeinfo.mat")

  rawDat = RawData()
  rawDat.retrieveRawDataChannels(data)
  
  for channel in rawDat.channels:
    channel.printRDC()

if __name__ == "__main__":
    main()



