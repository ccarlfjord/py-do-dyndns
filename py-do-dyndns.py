#!/bin/python3

import json
import requests

r = requests.get('https://ipinfo.io')
json = r.json()
print(json)
