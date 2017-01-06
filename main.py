#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import json
import requests
import time

# API_KEY = 'API_KEY'

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

ADRESSAPI = 'https://ipinfo.io'


def get_ip_adress():
    try:
        r = requests.get(ADRESSAPI).text
        return json.loads(r)['ip']
    except Exception as e:
        raise


def get_domain_info():
    pass

print(get_ip_adress())
