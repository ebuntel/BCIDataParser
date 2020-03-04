# BCIDataParser



## Documentation

Our BCIDataParser works in roughly two steps: 

1. Parsing the data from the .nirs, and probeinfo files.
2. Loading that data into the database.

Each of these steps will be explained in detail below. 

### How to run 
1. The first step is to get the .json file that has the datatabase login config information and put it in the src folder (same folder as main.py).
2. The second step in the process is to retrieve information from the probeinfo files,.nirs, description file. (The github repos contains these 3 files for example run. In the experiment, the files can be found in the Aurora folder.
Simply run main.py and choose the files with diaglog popup in the correct order.


### Parsing 
After running the above code rawDat (an instance of the RawDataCollection class) will contain all of the information you need. See the RawDataCollection section below for further details.

#### RawDataCollection

##### Fields

###### channels: 
This is a list object containing all of the channel objects which are retrieved by RawDataCollection's retrieveRawDataChannels method.

###### sources:
This is a list object containing all of the source objects which are retrieved by RawDataCollection's retrieveSourcesAndDetectors method.

###### detectors:
This is a list object containing all of the detector objects which are retrieved by RawDataCollection's retrieveSourcesAndDetectors method.

###### raw_data_list:
This is a list object containing all of the raw_data objects which are retrieved by RawDataCollection's retrieveRawData method.
