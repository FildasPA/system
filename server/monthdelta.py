#!/usr/bin/python
#-*- coding: utf-8 -*-

import datetime
import calendar

# Source : http://stackoverflow.com/a/22443132
def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m:
    	m = 12
    d = min(date.day, calendar.monthrange(y, m)[1])
    return date.replace(day=d, month=m, year=y)

print monthdelta(datetime.date.today(), -1)
