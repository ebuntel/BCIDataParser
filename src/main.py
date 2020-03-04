import numpy

from scipy.io import loadmat
from RawData import RawData
from DeviceSetup import DeviceSetup
from Subject import Subject


import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import psycopg2
import json
from RawDataCollection import RawDataCollection
import time


"""
Name: load
Description: this function loads probeInfor and nirs file into python
Parameter:either select the file with the diaglog popup by choosing probeInfo file, Nirsfile, description.json
or provide these parameter when executing the script
    python main.py <probeInfo> <Nirsfile> <description.json>
Output/result: 2 dictionaries: probeInfor, Nirs_Info
"""
def load(run_cnt):
    if len(sys.argv) != 4 or run_cnt==1:
        print('Please select probeInfo file')
        try:
            Tk().withdraw() #prevent opening a full diaglog
            filename=askopenfilename(title = "Select probeInfo file")
            probe_data = loadmat(filename)
            Tk().withdraw() #prevent opening a full diaglog
            filename=askopenfilename(title ="Select Nirs file")
            print('Please select nirs file')
            nirs_data = loadmat(filename)

            Tk().withdraw() #prevent opening a full diaglog
            config=askopenfilename(title= " Select description file. Ex: 201_AXCPT19_AS_description")
            print('Please select config file')
            return probe_data,nirs_data,config
        except:
            print("Wrong file type selection. Files are found in Aurora folder. Please select again in this order: ProbeInfo file, .nirs file, description file ")
            print("Example:201_AXCPT19_AS_probeInfo, 201_AXCPT19_AS_tm, 201_AXCPT19_AS_description ")
            exit()

    else:
        try:
            probe_data = loadmat(sys.argv[1])
            nirs_data = loadmat(sys.argv[2])
            config = loadmat(sys.argv[3])
            return probe_data, nirs_data, config
        except:
            print("Wrong file type selection. Files are found in Aurora folder. Please select again in this order: ProbeInfo file, .nirs file, description file ")
            print("Example:201_AXCPT19_AS_probeInfo, 201_AXCPT19_AS_tm, 201_AXCPT19_AS_description ")
            exit()

"""generate sql insert statement
    helper function for insert_query
"""
def generate_insert(table_name, values):
    if table_name!='subject':
        query ="INSERT INTO "+table_name +" VALUES (default, "
    else:
        query ="INSERT INTO "+table_name +" VALUES ("
    for v in values:
        if v=="NULL":
            query+="NULL"+","
        elif type(v)==str or type(v)==numpy.str:
            query +="\'"+v+"\'" +","
        else:
            query += str(v) +","
    query=query[:-1]
    pk_id_dict={'light_source':'pk_source_id', 'detector':'pk_detector_id', 'raw_data_channel':'pk_channel_id',\
    'device_setup':'pk_device_setup_id', 'raw_data':'pk_data_id','subject':'pk_subject_id'}
    query+=") RETURNING "+pk_id_dict[table_name]
    return query

"""
insert a new query when all fields match the database schema
"""
def insert_query(DB_connection, table_name, values):
    query = generate_insert(table_name, values)
    # print(query)
    cur= DB_connection.cursor()
    try:
        cur.execute(query, table_name)
        id = cur.fetchone()[0]
    except (Exception, psycopg2.Error) as error :
        print("ERROR MESSAGES "+ str(error))
        exit()

    # DB_connection.commit()
    return id


"""
bulk insert raw data points
Optimized function. It creates a transaction for every 10000 data points.
More than that it would overload the transaction and would get stuck in the request
"""
def insert_raw_data(DB_connection,values, cnt):
    cur = DB_connection.cursor()
    try:
        args_str = ','.join(cur.mogrify("(%s,%s,%s,%s,%s,%s,%s)", x).decode("utf-8") for x in values)
        query ="INSERT INTO raw_data (fk_device_setup, fk_subject,fk_channel, time_ms,value,time_source, bad_data_flag) VALUES " + args_str
        cur.execute(query)
    except (Exception, psycopg2.Error) as error :
        print("ERROR MESSAGES "+ str(error))
        exit()

    print("success parsing "+str(cnt*10000)+" raw data points")


"""
function that handles all the run, load, parse, upload to database
"""
def run(my_connection, run_cnt):
    data, nirs, config = load(run_cnt)
    rawDat = RawDataCollection()
    rawDat.retrieveRawDataChannels(data, nirs)
    rawDat.retrieveSourcesAndDetectors(data)
    rawDat.retrieveRawData(nirs)

    cursors_list=[]

    start_time=time.time()
    sources_list=rawDat.sources
    print("LOADING SOURCES")
    # insert sources into database
    for sd in sources_list:
        # print(sd.posX, sd.posY, sd.posZ, sd.name, sd.location_name_10_20)
        id= insert_query(my_connection, 'light_source', [sd.name, sd.posX, sd.posY, sd.posZ,str(sd.location_name_10_20) ] )
        sd.key=id
        # print(sd.key)
    print("time to finish parsing sources %f seconds" %(time.time()- start_time))

    detectors_list=rawDat.detectors
    start_time=time.time()
    print("LOADING DETECTORS")
    for sd in detectors_list:
        # print(sd.posX, sd.posY, sd.posZ, sd.name, sd.location_name_10_20)
        id= insert_query(my_connection, 'detector', [sd.name, sd.posX, sd.posY, sd.posZ,str(sd.location_name_10_20) ] )
        sd.key=id
        # print(sd.key)
    print("time to finish parsing detectors %f seconds"  %(time.time()- start_time))

    print("LOADING CHANNELS")
    channels_list=rawDat.channels
    start_time=time.time()
    for c in channels_list:
        c.name="S"+str(c.source)+"-D"+str(c.detector)+"-"+str(c.wavelength)
        # print(c.source, c.detector, c.channel_num,c.badDataFlag, c.name, c.wavelength)
        for d in detectors_list:
            if int(d.name[1])==c.detector:
                fk_detector=d.key
        for s in sources_list:
            if int(s.name[1])==c.source:
                fk_source=s.key
        # print(fk_detector, fk_source)
        id= insert_query(my_connection, 'raw_data_channel', [fk_source, fk_detector, 'NULL', 'NULL', c.wavelength, c.name, c.badDataFlag] )
        c.key=id
    print("time to finish parsing channels %f seconds" %(time.time()- start_time))

    print("LOADING RAW DATA")
    # insert raw data
    raw_data_list=rawDat.raw_data_list
    dict={}
    for channel in channels_list:
        dict[(channel.channel_num, channel.wavelength)]=channel.key
    # insert device setup
    device_setup=DeviceSetup()
    # modify update_rate_HZ
    #insert
    fk_device_setup = insert_query(my_connection, 'device_setup', ["NULL","NULL", "NULL","NULL","NULL","NULL", "NULL","NULL",device_setup.update_rate_HZ, "NULL"])

    # insert Subject
    subject=Subject()
    # parse subject meaningfulname
    with open(config) as f:
        data = json.load(f)
    subject.key=data['subject']
    #insert subject to database
    fk_subject = insert_query(my_connection, 'subject', [subject.key,subject.bad_data_flag])

    # add raw data into db
    raw_data_insert_list=[]
    cnt=0
    times=0
    start_time=time.time()
    for data_point in raw_data_list:
        fk_channel= dict[(data_point.channel, data_point.wavelength)]
        raw_data_insert_list.append([fk_device_setup, fk_subject, fk_channel, \
        data_point.time_s, data_point.value, data_point.time_source, data_point.bad_data_flag])

        cnt+=1
        if cnt==10000:
            times+=1
            insert_raw_data(my_connection,raw_data_insert_list, times)
            raw_data_insert_list=[]
            cnt=0
    end_time=time.time()
    print("time to finish parsing raw data %d seconds" %(time.time()- start_time))

    print("Parsing completed. Do you want to commit to database? y for YES/n for NO")
    user_input=input()
    if user_input=='y':
        try:
            print("uploading...")
            start_time=time.time()
            my_connection.commit()
            print("time to finish committing to database %f seconds" %(time.time()-start_time))
            print("successful uploading to database")
        except (Exception, psycopg2.Error) as error :
            my_connection.rollback()
            print("Committing failed. Abort commits to database")
            print("Error: " + error)
    else:
        print("Abort committing to database")

def main():
    with open('databaseconfig.json') as f:
        data = json.load(f)
    try:
        my_connection = psycopg2.connect( host=data['host'], user=data['user'], password=data['password'], dbname=data['dbname'] )
        # Print PostgreSQL Connection properties
        print ( my_connection.get_dsn_parameters(),"\n")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    print("Starting script")
    run(my_connection,0)
    print("Do you want to parse another experiment? y for YES/ n for NO")
    user_input=input()
    if user_input=='y':
        run(my_connection,1)
    else:
        if my_connection is not None:
            my_connection.close()
            exit()





if __name__== "__main__":
  main()
