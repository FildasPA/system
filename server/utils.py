#!/usr/bin/python
#-*- coding: utf-8 -*-


import time


def get_current_time():
    t = time.localtime()
    date = "{year}-{month}-{day} {hour}:{minu}:{sec}".format(year=t.tm_year, month=t.tm_mon, day=t.tm_mday, hour=t.tm_hour, minu=t.tm_min, sec=t.tm_sec)
    return date
