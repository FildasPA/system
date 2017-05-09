#!/usr/bin/python
#-*- coding: utf-8 -*-

# from collect.py import *
from flask import Flask
from collect import *

app = Flask(__name__)

@app.route('/info')
def print_info():
    info = get_system_information()
    return str(info)

if __name__ == "__main__":
    app.run()
