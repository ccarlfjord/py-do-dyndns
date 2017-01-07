#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import json
import requests
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
ADRESSAPI = 'https://ipinfo.io'


def get_ip_adress():
    try:
        r = requests.get(ADRESSAPI).text
        return json.loads(r)['ip']
    except Exception as e:
        raise


def get_domain_info():
    API_KEY = open('.API_KEY', 'r').read().rstrip()
    return API_KEY

print(get_domain_info())
