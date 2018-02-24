#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import logging
import os
import argparse
import time
import yaml
import sys

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
        r = requests.get(url, headers=self.api_header)
        if r.status_code != 200:
            log.error(
                "Something went wrong. Error code: {0}. Retrying..." .format(r.status_code))
            time.sleep(1)
            self.get_record()
        else:
            records = r.json()
            for record in records['domain_records']:
                if record['name'] == self.record:
                    return record

    def get_ip(self):
        r = requests.get(self.adress_api)
        if r.status_code != 200:
            log.error(
                "Something went wrong. Error code: {0}. Retrying..." .format(r.status_code))
            time.sleep(1)
            self.get_ip()
        else:
            data = r.json()
            log.info("Found my ip {}" .format(data['ip']))
            return data['ip']

    def update_record(self):
        record = self.get_record()
        ip = self.get_ip()
        url = "{0}/domains/{1}/records/{2}" .format(
            self.do_api_url, self.domain, record['id'])
        d = json.dumps({'data': ip})
        h = {'Content-Type': 'application/json'}
        h.update(self.api_header)

        if record['data'] == ip:
            log.info(
                "IP-adress for {0}.{1} already set to {2}, returning to sleep."
                .format(self.record, self.domain, ip))
            return
        r = requests.put(url, data=d, headers=h)
        if r.status_code != 200:
            log.error(
                "Updating record failed with error code: {0} on {1}" .format(r.status_code, url))
            time.sleep(1)
            self.update_record()
        else:
            log.info("Done updating record {0}.{1} to {2}" .format(self.record, self.domain, ip))
            return r.status_code


def main():
    LOGFORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOGFORMAT)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", default="settings.yaml")
    args = parser.parse_args()
    f = open(os.path.join(os.path.dirname(__file__), args.config))
    cfg = yaml.load(f)

    adress_api = cfg['adress_api']
    domain = cfg['domain']
    record = cfg['record']
    api_key = cfg['api_key']
    sleep = cfg['sleep']
    if not api_key:
        log.error("api_key is empty, add your DigitalOcean api key to settings.yaml")
        sys.exit(1)

    while True:
        log.info("Starting update of {0}.{1}" .format(record, domain))
        d = Domain(adress_api, domain, record, api_key)
        d.update_record()
        time.sleep(sleep)


if __name__ == '__main__':
    main()
