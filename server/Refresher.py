#!/usr/bin/python
#-*- coding: utf-8 -*-

import sqlite3 as lite
import time
import datetime


def monthdelta(date, delta):
        m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
        if not m: m = 12
        d = min(date.day, [31,29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
        return date.replace(day=d,month=m, year=y)


def refresh():
    con = lite.connect('BDD.db')


    with con:

        #temps = time.localtime();
        #timee = "{year}-{month}-{day}".format(year=temps.tm_year, month=temps.tm_mon, day=temps.tm_mday, 	hour=temps.tm_hour, minu=temps.tm_min, sec=temps.tm_sec)

        timee = monthdelta(datetime.datetime.now(), -1)
        timeee = "{year}-{month}-{day} {hour}:{minu}:{sec}".format(year=timee.year, month=timee.month, day=timee.day, hour=timee.hour, minu=timee.minute, sec=timee.second)
        #voir comment faire avec timee.year time.month etc
        print timeee

        cur = con.cursor()
        cur.execute("DELETE FROM infosys WHERE date < :datee;", {'datee': timeee})
        cur.execute("DELETE FROM users WHERE date < :datee;", {'datee': timeee})
        cur.execute("DELETE FROM cert WHERE date < :datee;", {'datee': timeee})

