#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
import datetime
import sqlite3 as lite


def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month) + delta-1) // 12
    if not m:
        m = 12
    d = min(date.day, [31,
            29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)


con = lite.connect('BDD.db')

newdate = monthdelta(datetime.datetime.now(), -1)
datetocompare = "{year}-{month}-{day} {hour}:{minute}:{sec}".format(year=newdate.year, month=newdate.month, day=newdate.day, hour=newdate.hour, minute=newdate.minute, sec=newdate.second)

cur = con.cursor()
cur.execute("DELETE FROM infosys WHERE date < :datee;", {'datee': datetocompare})
cur.execute("DELETE FROM cert WHERE date < :datee;", {'datee': datetocompare})
