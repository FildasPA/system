#!/usr/bin/python
#-*- coding: utf-8 -*-

# Ouvre un serveur web
# Traite les informations des requêtes reçues

from flask import Flask
from flask import request
import InfoProcessing
import Config

app = Flask(__name__)


@app.route('/' + Config.SERVER_SEND_INFO, methods=['POST'])
def catch_info():
    if request.method != 'POST':
        content = "Error: you must send a POST request"
    else:
        info = dict(request.form)
        for i in info:
            info[i] = str(info[i][0])
        InfoProcessing.process_info(info)
        content = "Information received"
    return str(content)


if __name__ == "__main__":
    app.run()
