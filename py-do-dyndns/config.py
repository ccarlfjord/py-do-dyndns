#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml

with open(os.path.join(os.path.dirname(__file__), './settings.yaml')) as f:
    cfg = yaml.load(f)

adressapi = cfg['adressapi']
domain = cfg['domain']
record = cfg['record']
api_key = cfg['api_key']
