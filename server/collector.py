#!/usr/bin/python
#-*- coding: utf-8 -*-

# Ouvre un serveur web
# Traite les informations des requêtes reçues

# from collect.py import *
from flask import Flask
from flask import request
from sensors import *

app = Flask(__name__)

@app.route('/info', methods=['POST'])
def print_info():
    if request.method == 'POST':
        content = request.form

        # print "post!"
        # if valid_login(request.form['username'],
        #                request.form['password']):
            # return log_the_user_in(request.form['username'])
        # else:
            # error = 'Invalid username/password'
        # info = request.data
        # info = request.values
    else:
        content = "Error: you must send a POST request"
        # info = get_system_information()
    return str(content)

if __name__ == "__main__":
    app.run()
