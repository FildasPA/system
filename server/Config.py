#!/usr/bin/python
#-*- coding: utf-8 -*-

import read_config


def replace_value(config, section, key, current_value):
    new_value = config.get(section, key)
    if new_value:
        return new_value
    return current_value


DATA_DIR    = 'local'
CONFIG_FILE = DATA_DIR + '/sys.conf'
DB_FILE     = DATA_DIR + '/sys.db'

config = read_config.read_config()

SERVER_ADDRESS   = replace_value(config, 'Server', 'address', "http://localhost:5000")
SERVER_SEND_INFO = replace_value(config, 'Server', 'send_info', "sendinfo")
SERVER_SEND_INFO_URL = "{}/{}".format(SERVER_ADDRESS, SERVER_SEND_INFO)
