#!/usr/bin/python
#-*- coding: utf-8 -*-

from flask import Flask
from ../collect.py import
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def print_infos():
    return
