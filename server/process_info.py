#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
import os.path
import sqlite3 as sqlite
import ConfigParser


SECTION = 'Crisis'
CONFIG_FILE = 'local/sys.conf'


def process_info(info):
    save_info(info)
    check_crisis(info)


def get_current_time():
    t = time.localtime()
    date = "{year}-{month}-{day} {hour}:{minu}:{sec}".format(year=t.tm_year, month=t.tm_mon, day=t.tm_mday, hour=t.tm_hour, minu=t.tm_min, sec=t.tm_sec)
    return date


def save_info(info):
    """Save information in database"""
    con = sqlite.connect('local/sys.db')
    with con:
        cur = con.cursor()
        t = get_current_time()
        cur.execute("INSERT INTO infosys (date, hostname, processes, users, cpu, ram, disk, swap) VALUES (:date, :hostname, :processes, :users, :cpu, :ram, :disk, :swap);", {'date': t, 'hostname': info['hostname'], 'processes': info['processes'], 'users': info['users'], 'cpu': info['cpu'], 'ram': info['ram'], 'disk': info['disk'], 'swap': info['swap']})
        con.commit()


def write_config_file(filename, config):
    config.add_section(SECTION)
    config.set(SECTION, "no_response", "30")
    config.set(SECTION, "cpu", "90")
    config.set(SECTION, "ram", "100")
    config.set(SECTION, "disk", "95")
    config.write(open(filename, 'w'))


def read_config():
    """Read config file, or write one if there is none"""
    config = ConfigParser.ConfigParser()
    if not os.path.isfile(CONFIG_FILE):
        write_config_file(CONFIG_FILE, config)
    config.read(CONFIG_FILE)
    if SECTION not in config.sections():
        write_config_file(CONFIG_FILE, config)
    return config


def check_crisis(info):
    """ description """
    config = read_config()
    crisis = {}
    for option in config.items(SECTION):
        if option[0] not in info:
            continue
        # print "{} : {}".format(option[0], option[1])
        if info[option[0]] >= option[1]:
            crisis[option[0]] = info[option[0]]
        # value = info[option[0]]
    # if crisis:

