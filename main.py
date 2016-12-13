#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import logging
import sys
import json
import requests
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

adressApi = 'https://api.ipify.org'

class GetIPAddr(object):
    def get_ip():
        f = requests.get(adressApi).text
        return f
    def show_me():
        print(GetIPAddr.get_ip())

GetIPAddr.show_me()
