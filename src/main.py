import numpy as np

from scipy.io import loadmat
from RawDataCollection import RawDataCollection

def main():
  print("Starting script")
  data = loadmat("223_AXCPT19_CH_probeinfo.mat")
  nirs = loadmat("test_nirs.nirs")

  rawDat = RawDataCollection()
  rawDat.retrieveRawDataChannels(data, nirs)
  rawDat.retrieveSourcesAndDetectors(data)
  rawDat.retrieveRawData(nirs)
  
  for dat in rawDat.getRawDataPoints():
    dat.printDataPoint()

if __name__ == "__main__":
    main()



