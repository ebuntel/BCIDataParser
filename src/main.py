import numpy as np

from scipy.io import loadmat
from RawData import RawData

def main():
  data = loadmat("223_AXCPT19_CH_probeinfo.mat")

  rawDat = RawData()
  rawDat.retrieveRawDataChannels(data)
  
  for channel in rawDat.getChannels():
    channel.printRDC()

if __name__ == "__main__":
    main()



