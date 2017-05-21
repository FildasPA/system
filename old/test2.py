#!/usr/bin/python
#-*- coding: utf-8 -*-

import sqlite3 as sqlite

con = sqlite.connect('local/sys.db')
cur = con.cursor()
res = cur.execute("SELECT * FROM infosys;").fetchall()
for i in res:
	print i
con.close()
# cur.execute("ALTER TABLE infosys ADD COLUMN swap double")
# cur.commit()
# cur.execute("UPDATE infosys SET date = '2017-3-8' WHERE nbProcessus = 219;")
# con.commit()
