#!/usr/bin/python
#-*- coding: utf-8 -*-

import os.path
import sqlite3 as sqlite
import utils
import CrisisChecker
# from mail import send_mails
import Config


def process_info(info):
    save_info(info)
    crises = CrisisChecker.get_crises(info)
    # if crises:
    #     send_crises_to_mail(crises)


def save_info(info):
    """Save information in database"""
    con = sqlite.connect(Config.DB_FILE)
    with con:
        cur = con.cursor()
        t = utils.get_current_time()
        cur.execute("INSERT INTO infosys (date, hostname, processes, users, cpu, ram, disk, swap) VALUES (:date, :hostname, :processes, :users, :cpu, :ram, :disk, :swap);", {'date': t, 'hostname': info['hostname'], 'processes': info['processes'], 'users': info['users'], 'cpu': info['cpu'], 'ram': info['ram'], 'disk': info['disk'], 'swap': info['swap']})
        con.commit()
