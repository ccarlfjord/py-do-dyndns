#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import requests
from datetime import datetime
import config

ADRESSAPI = config.adressapi
DOMAIN = config.domain
API_KEY = config.api_key
RECORD = config.record

DO_API_URL = "https://api.digitalocean.com/v2"
DO_API_HEADER = {'Authorization': "Bearer {0}" .format(API_KEY)}

ts = str(datetime.now()).split('.')[0]


def get_ip_adress():
    req = requests.get(ADRESSAPI)
    result = req.json()

    try:
        return result['ip']
    except Exception as e:
        raise


def get_domain(name=DOMAIN):
    url = "%s/domains/" % (DO_API_URL)

    try:
        req = requests.get(url, headers=DO_API_HEADER)
        result = req.json()

        for domain in result['domains']:
            if domain['name'] == name:
                return domain
    except Exception as e:
        raise


def get_record(domain, name=RECORD):
    print()
    url = "%s/domains/%s/records" % (DO_API_URL, domain['name'])

    try:
        req = requests.get(url, headers=DO_API_HEADER)
        result = req.json()

        for record in result['domain_records']:
            if record['name'] == name:
                return record
    except Exception as e:
        raise


def set_record_ip(domain, record, ipaddr):
    url = "%s/domains/%s/records/%s" % (DO_API_URL, domain['name'], record['id'])
    data = json.dumps({'data': ipaddr}).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    headers.update(DO_API_HEADER)

    req = requests.put(url, data=data, headers=headers)

if __name__ == '__main__':
    try:
        print("%s: Updating %s.%s" % (ts, RECORD, DOMAIN), end="")
        ipaddr = get_ip_adress()
        domain = get_domain()
        record = get_record(domain)
        if record['data'] == ipaddr:
            print("%s: Record %s.%s already set to %s. \n" % (ts, record['name'], domain['name'], ipaddr))
        else:
            set_record_ip(domain, record, ipaddr)
    except Exception as e:
        raise
