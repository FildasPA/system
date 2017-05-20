#!/usr/bin/python
#-*- coding: utf-8 -*-

# Ouvre un serveur web
# Traite les informations des requêtes reçues

from flask import Flask
from flask import request
import process_info

app = Flask(__name__)


@app.route('/sendinfo', methods=['POST'])
def catch_info():
    if request.method == 'POST':
        content = dict(request.form)
        for i in content:
            content[i] = str(content[i][0])
        process_info.process_info(content)
    else:
        content = "Error: you must send a POST request"
    return str(content)


if __name__ == "__main__":
    app.run()
