from Subject import Subject
from Event import Event

class EventData:
    """Top-level class holding subject and event data.

    Attributes:
        name: EventData name
        start_time: Event start time
        end_time: Event end time
        sub: Event subject
        event: Instance of the event class
        bad_data_flag: Flag indicating whether the data is bad or not
        time_source: 
        long_desc: Description of this event
    """

    def __init__(self):
        self.name = ""
        self.start_time = 0.0
        self.end_time = 0.0
        self.sub = None
        self.event = None
        self.bad_data_flag = False
        self.time_source = ""
        self.long_desc = ""

    # Getters and Setters

    def getName(self):
        return self.name

    def getStart(self):
        return self.start_time

    def getEnd(self):
        return self.end_time

    def getSubject(self):
        return self.sub

    def getEvent(self):
        return self.event

    def getDataFlag(self):
        return self.bad_data_flag

    def getTimeSource(self):
        return self.time_source

    def getLongDesc(self):
        return self.long_desc

    def setName(self, newName):
        self.name = newName

    def setStart(self, time):
        self.start_time = time

    def setEnd(self, time):
        self.end_time = time

    def setSubject(self, sub):
        self.sub = sub

    def setEvent(self, event):
        self.event = event

    def setDataFlag(self, flag):
        self.bad_data_flag = flag

    def setTimeSource(self, time):
        self.time_source = time

    def setLongDesc(self, desc):
        self.long_desc = desc

    #