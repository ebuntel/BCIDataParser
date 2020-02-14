import numpy as np

from scipy.io import loadmat
from RawData import RawData
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename


"""

Name: load
Description: this function loads probeInfor and nirs file into python
Parameter:either select the file with the diaglog popup by choosing probeInfo file and Nirsfile
or provide these parameter when executing the script
    python main.py <probeInfo> <Nirsfile>
Output/result: 2 dictionaries: probeInfor, Nirs_Info
"""
def load():
    if len(sys.argv) != 3:
        print('Please select probeInfo file')
        Tk().withdraw() #prevent opening a full diaglog
        filename=askopenfilename()
        probe_data = loadmat(filename)
        Tk().withdraw() #prevent opening a full diaglog
        filename=askopenfilename()
        print('Please select nirs file')
        nirs_data = loadmat(filename)
        return probe_data,nirs_data
    else:
        probe_data = loadmat(sys.argv[1])
        nirs_data = loadmat(sys.argv[2])
        return probe_data, nirs_data

# def testSourceAndDetectorPrints():
#     src = Source(1.0, 2.0, -4.5, "george", "feckoff")
#     det = Detector(-1100, 7.8, 4, "Arnold", "det feckoff")
#     src.printSource()
#     det.printDetector()

def main():
  #get probe_data, nirs_data
  #pass in nirs_data to parse other information
  probe_data, nirs_data  = load()
  rawDat = RawData()
  rawDat.retrieveRawDataChannels(probe_data)

  for channel in rawDat.channels:
    channel.printRDC()




if __name__== "__main__":
  main()
