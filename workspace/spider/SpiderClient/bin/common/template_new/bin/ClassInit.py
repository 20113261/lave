#!/usr/bin/env python
#coding:utf-8

import sys

from HtmlFlight import *
from HtmlRoundFlight import *
from HtmlTrain import *
from HtmlBus import *
from HtmlRoom import *
from HtmlCar import *
from JsonBus import *
from JsonFlight import *
from JsonTrain import *
from JsonRoom import *
from JsonCar import *
from PageTreeDict import *

class ClassInit(PageTreeDict, HtmlFlight, HtmlRoundFlight, HtmlTrain, HtmlBus, \
        HtmlRoom, HtmlCar, JsonBus, JsonFlight, JsonTrain, JsonRoom, JsonCar):

    def __init__(self):
        pass

    def test(self):
        print 'The class is OK!'



if __name__ == '__main__':

    ci = ClassInit()

    print ci.test()
