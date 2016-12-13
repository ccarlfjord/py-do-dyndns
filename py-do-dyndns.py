#!/bin/python3

import logging
import sys
import json
import requests

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
class GetIpAddr(object):

    r = requests.get('https://ipinfo.io')
    json = r.json()
    # print(json)
    

x = GetIpAddr()
