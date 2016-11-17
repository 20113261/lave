#!/usr/bin/env python
#coding:utf-8

import sys


#年龄是前开后闭区间
source_age_dict = {
    'elongHotel':{
        'adult': '19',
        'children':'2_18',
        'infant':''
    },
    'travelfusionApi':{
        'adult':'18',
        'children':'',
        'infant':''
    }
}




class Passengers:

    def __init__(self, source, agestr):
        self._dict = source_age_dict
        self.adult = dict()
        self.children = dict()
        self.infant = dict()
        self.source = source
        self.agelist = agestr.split('_')
        self.Cal_adult()
        self.Cal_children()
        self.Cal_infant()

    def Cal_adult(self):
        adultStr = self._dict.get(self.source).get('adult')
        if adultStr != '':
            self.adult['num'] = len([age for age in self.agelist if int(age) >= int(adultStr) or int(age) == -1]) 
            self.adult['age'] = filter(lambda x:int(x) >= int(adultStr) or int(x) == -1, self.agelist)

    def Cal_children(self):
        childrenStr = self._dict.get(self.source).get('children')
        if childrenStr != '':
            self.children['num'] = len([age for age in self.agelist if int(age) >= int(childrenStr.split('_')[0]) and int(age) < int(childrenStr.split('_')[1])]) 
            self.children['age'] = filter(lambda x:int(x) >= int(childrenStr.split('_')[0]) and int(x) < int(childrenStr.split('_')[1]), self.agelist)

    def Cal_infant(self):
        infantStr = self._dict.get(self.source).get('infant')
        if infantStr != '':
            self.infant['num'] = len([age for age in self.agelist if int(age) >= int(infantStr.split('_')[0]) and int(age) < int(infantStr.split('_')[1])]) 
            self.infant['age'] = filter(lambda x:int(x) >= int(infantStr.split('_')[0]) and int(x) < int(infantStr.split('_')[1]), self.agelist)

