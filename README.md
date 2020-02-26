# BCIDataParser



## Documentation

Our BCIDataParser works in roughly two steps: 

1. Parsing the data from the .nirs, and probeinfo files.
2. Loading that data into the database.

Each of these steps will be explained in detail below. 

### Parsing 

The first step in the process is to retrieve information from the .nirs and probeinfo files, and to make the data easily available for the next step. 

Here is a quick example of how to parse the information you'll need to upload to the database:

```python
data = loadmat("test_probeinfo.mat")
nirs = loadmat("test_nirs.nirs")

rawDat = RawDataCollection()
rawDat.retrieveRawDataChannels(data, nirs)
rawDat.retrieveSourcesAndDetectors(data)
rawDat.retrieveRawData(nirs)
```

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
