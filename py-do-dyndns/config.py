#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import yaml
from datetime import datetime

ts = str(datetime.now()).split('.')[0]

with open(os.path.join(os.path.dirname(__file__), './settings.yaml')) as f:
    cfg = yaml.load(f)

if cfg['api_key'] != None:
    adressapi = cfg['adressapi']
    domain = cfg['domain']
    record = cfg['record']
    api_key = cfg['api_key']
else:
    print(
        "{ts}: api_key is empty, add your DigitalOcean api key to settings.yaml" .format(ts=ts))
    sys.exit(1)
