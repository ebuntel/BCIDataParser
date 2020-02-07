from scipy.io import loadmat
# from subject import Subject
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#
#
#

"""

Name: load
Description: this function loads nirs file into python
Assumption:N/A
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


def main():
  # sub = Subject()
  data = load()
  sub.getDetectors(data)
  sub.printDetectors()
  sub.getSources(data)
  sub.printSources()

if __name__== "__main__":
  main()
