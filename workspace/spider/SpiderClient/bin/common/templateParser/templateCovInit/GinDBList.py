#!/usr/bin/env python
#coding:utf-8

from .BusDB import*
from .TrainDB import *
from .RoundFlightDB import *
from .HotelDB import *
from .CarDB import *
from .RoomDB import *
from .FlightDB import *

class GinDBList(object):

    def __init__(self):
        self.busDB = BusDB()
        self.carDB = CarDB()
        self.hotelDB = HotelDB()
        self.roomDB = RoomDB()
        self.roundFlightDB = RoundFlightDB()
        self.trainDB = TrainDB()
        self.flightDB = FlightDB()
        self.result = []

    def GetInDBList(self, type, dictList):
        
        if type.lower() == 'bus':
            self.result = self.busDB.busTupleList(dictList)
        elif type.lower() == 'flight':
            self.result = self.flightDB.flightTupleList(dictList)
        elif type.lower() == 'train':
            self.result = self.trainDB.trainTupleList(dictList)
        elif type.lower() == 'roundflight':
            self.result = self.roundFlightDB.RoundFlightTupleList(dictList)
        elif type.lower() == 'car':
            self.result = self.carDB.carTupleList(dictList)
        elif type.lower() == 'room':
            self.result = self.roomDB.roomTupleList(dictList)
        elif type.lower() == 'hotel':
            self.result = self.hotelDB.hotelTupleList(dictList)
        else:
            pass

        return self.result

