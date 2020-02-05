from scipy.io import loadmat
from subject import Subject

#
#
#
def main():
  sub = Subject()
  data = loadmat('test_nirs.nirs')
  sub.getDetectors(data)
  sub.printDetectors()
  sub.getSources(data)
  sub.printSources()

if __name__== "__main__":
  main()