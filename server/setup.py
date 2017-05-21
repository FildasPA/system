#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sqlite3 as sqlite
import Config


def create_db():
	con = sqlite.connect(Config.DB_FILE)
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE infosys (date datetime, hostname text, processes int, users int, cpu double, ram double, disk double, swap double, PRIMARY KEY (date, hostname));")
		cur.execute("CREATE TABLE certalert (date datetime PRIMARY KEY, title text);")


if not os.path.exists(Config.DATA_DIR):
	os.makedirs(Config.DATA_DIR)
create_db()
