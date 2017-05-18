#!/usr/bin/python
#coding: utf-8

# Envoie les informations systèmes au serveur
# Pour cela, envoie une requête POST

import ast
import urllib2
import requests
from bs4 import BeautifulSoup
from collect import get_system_information

url = 'http://localhost:5000/info'
data = get_system_information()
r = requests.post(url, data = data)
print r.text
# print r.content()
# print data
# print r
# content = urllib2.urlopen(url).read()
# soup = BeautifulSoup(content, 'lxml')
# info = ast.literal_eval(soup.get_text())

# print info
