#!venv/bin/python
#!venv/bin/python

import psycopg2
#!venv/bin/python
#import pdb
#pdb.set_trace()
from __future__ import print_function
import sys
import xml.etree.ElementTree as ET
import pg8000
from os import listdir
from os.path import isfile, join
import time
from six import b, BytesIO
#from io import BytesIO

#NOTE: needs info that is being parsed passed put in where indicated

begin = time.time() #start timer

print('beginning run:', time.asctime(time.localtime(begin)))

try:
    connectionInfo = "" #parsing information from .nRIS file that has been parsed
    '''
    #may need this for connecting
    connection = psycopg2.connect(user = "postgres",
                                      password = "jhA-j4X-ZqI-LTX",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "postgres_db")
    '''
    if connectionInfo is None:
            print('No connection information found in config, ending parse.') #no connection found, stop program
            return
    connection = getOpenConnection(connectionInfo) #establish connection
    cursor = connection.cursor() #establish cursor to interact with database
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    # This is where a query would go
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            end = time.time() #stop timer
            print('run time:', str(end - begin)) #print run time
            cursor.close() #close cursor
            connection.close() #close connection

            print("PostgreSQL connection is closed")
