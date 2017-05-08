#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests

# r = requests.get('https://api.github.com/events')
r = requests.get('http://127.0.0.1:5000/')
print r.text
