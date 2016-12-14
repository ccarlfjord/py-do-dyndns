#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import sys
import json
import requests
import time

#API_KEY = 'API_KEY'

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class FetchIp(object):

    def __init__(self):
        self.api = 'https://api.ipify.org'
        self.data = requests.get(self.api).text

class DoApiKey(object):
    def __init__(self, *arg):
        self.file = 'API_KEY'
        self.data = open(self.file, 'r').readline().rstrip()
        
x = FetchIp().data
f = DoApiKey().data

y = 0
while y < 3:
    print(x)
    print(f)
    y +=1
    # def DigitalOcean():
    #     apiKey = open('./API_KEY', 'r').readline().rstrip()
    #     return apiKey
