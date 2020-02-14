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
Description: this function loads nirs file into python
Parameter:either provide a fileName when executing the script or select the file
with the diaglog popup
Output/result: a dictionary object that has data imported from Matlab file
"""
def load():
    if len(sys.argv) != 2:
        print('Please select a file for parsing')
        Tk().withdraw() #prevent opening a full diaglog
        filename=askopenfilename()
        data = loadmat(filename)
        return data
    else:
        data = loadmat(sys.argv[1])
        return data

# def testSourceAndDetectorPrints():
#     src = Source(1.0, 2.0, -4.5, "george", "feckoff")
#     det = Detector(-1100, 7.8, 4, "Arnold", "det feckoff")
#     src.printSource()
#     det.printDetector()

def main():
  data = load()
  rawDat = RawData()
  rawDat.retrieveRawDataChannels(data)

  for channel in rawDat.channels:
    channel.printRDC()




if __name__== "__main__":
  main()
