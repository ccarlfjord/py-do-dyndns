#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import json
import requests
import time

# API_KEY = 'API_KEY'

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

CHECKIPAPI = 'https://ipinfo.io'

def get_ip_adress():
    _r = requests.get(CHECKIPAPI).text
    return json.loads(_r)['ip']

def get_domain_info():
    pass

print(get_ip_adress())
# def DigitalOcean():
#     apiKey = open('./API_KEY', 'r').readline().rstrip()
#     return apiKey
