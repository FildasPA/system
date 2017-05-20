#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sqlite3 as sqlite


def create_db():
	con = sqlite.connect('local/sys.db')
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE infosys (date datetime, hostname text, processes int, users int, cpu double, ram double, disk double, swap double, PRIMARY KEY (date, hostname));")
		cur.execute("CREATE TABLE certalert (date datetime PRIMARY KEY, title text);")


if not os.path.exists('local'):
	os.makedirs('local')
create_db()

