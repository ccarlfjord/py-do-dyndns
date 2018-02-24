#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import logging
import os
import argparse
import time
import yaml

log = logging.getLogger("do-dyndns")
log.setLevel(logging.INFO)


class Domain:

    def __init__(self, adress_api, domain, record, api_key):
        self.adress_api = adress_api
        self.domain = domain
        self.record = record
        self.api_key = api_key
        self.api_header = {'Authorization': "Bearer {0}" .format(self.api_key)}
        self.do_api_url = "https://api.digitalocean.com/v2"

    def get_record(self):
        url = "{0}/domains/{1}/records" .format(self.do_api_url, self.domain)
        log.info("Fetching records from {0}" .format(url))
        r = requests.get(url, headers=self.api_header)
        if r.status_code != 200:
            log.error(
                "Something went wrong. Error code: {0} \nRetrying..." .format(r.status_code))
            self.get_record()
        else:
            records = r.json()
            for record in records['domain_records']:
                if record['name'] == self.record:
                    return record

    def get_ip(self):
        log.info("Getting ip address")
        r = requests.get(self.adress_api)
        if r.status_code != 200:
            log.error(
                "Something went wrong. Error code: {0} \nRetrying..." .format(r.status_code))
            self.get_ip()
        else:
            data = r.json()
            return data['ip']

    def update_record(self):
        log.info("Updating record")
        record = self.get_record()
        ip = self.get_ip()
        url = "{0}/domains/{1}/records/{2}" .format(
            self.do_api_url, self.domain, record['id'])
        d = json.dumps({'data': ip})
        h = {'Content-Type': 'application/json'}
        h.update(self.api_header)

        if record['data'] == ip:
            log.info("IP address for {0} already set to {1}" .format(self.record, ip))
            return
        r = requests.put(url, data=d, headers=h)
        if r.status_code != 200:
            log.error(
                "Updating record failed with error code: {0} on {1}" .format(r.status_code, url))
            self.update_record()
        else:
            return r.status_code


class Config:
    f = open(os.path.join(os.getcwd(), 'settings.yaml'))
    cfg = yaml.load(f)

    adress_api = cfg['adress_api']
    domain = cfg['domain']
    record = cfg['record']
    api_key = cfg['api_key']

    if api_key is None:
        log.error(
            "api_key is empty, add your DigitalOcean api key to settings.yaml")


def main():
    LOGFORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOGFORMAT)
    while True:
        log.info("Loading config")
        cfg = Config()
        d = Domain(cfg.adress_api, cfg.domain, cfg.record, cfg.api_key)
        d.update_record()
        log.info("Sleeping")
        time.sleep(1200)


if __name__ == '__main__':
    main()
