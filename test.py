#!/usr/bin/python
#-*- coding: utf-8 -*-

import sqlite3 as sqlite

con = sqlite.connect('BDD.db')
cur = con.cursor()
# cur.execute("UPDATE infosys SET date = '2017-3-8' WHERE nbProcessus = 219;")
# con.commit()
cur.execute("SELECT * FROM infosys;").fetchall()
con.close()
