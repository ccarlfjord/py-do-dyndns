#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import logging
import sys
import json
import requests
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class GetIpAdress(object):
    
    def __init__(self):
        # self.GetIpAdress = GetIpAdress
        self.show_me = GetIpAdress.show_me()
        # self.get_ip = GetIpAdress.get_ip()
        self.DigitalOcean = GetIpAdress.DigitalOcean()
    
    def get_ip():
        adressApi = 'https://api.ipify.org'
        f = requests.get(adressApi).text
        return f

    def DigitalOcean():
        apiKey = open('./API_KEY', 'r').readline().rstrip()
        print(apiKey)
        
    def show_me():
        print(GetIpAdress.get_ip())
        #print(GetIpAdress.DigitalOcean())

GetIpAdress()
