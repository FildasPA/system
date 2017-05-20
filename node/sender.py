#!/usr/bin/python
#coding: utf-8

# Envoie les informations systèmes au serveur à l'aide d'une requête POST

import requests
from sensors import get_system_information

def send_info(url, data):
	r = requests.post(url, data = data)
	print r.text


if __name__ == "__main__":
	url = 'http://localhost:5000/sendinfo'
	data = get_system_information()
	send_info(url, data)
