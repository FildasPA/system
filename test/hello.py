#!/usr/bin/python
#-*- coding: utf-8 -*-

# from collect.py import *
from flask import Flask
from coll
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def print_infos():
    return str(get_system_informations())

if __name__ == "__main__":
    app.run()
