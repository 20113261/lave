#!/usr/bin/env python 
#coding:utf-8



import os
import random
from user_agent import generate_user_agent

def GetUserAgent():

    randomNumber = random.randint(1, 100)
    userAgent = ''
    if randomNumber < 15:
        userAgent = generate_user_agent(navigator='firefox')
    elif randomNumber >= 15 and randomNumber < 70:
        userAgent = generate_user_agent(navigator='chrome')
    else:
        userAgent = generate_user_agent(navigator='ie')

    return userAgent


