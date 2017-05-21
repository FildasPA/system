#!/usr/bin/python
#-*- coding: utf-8 -*-

import sqlite3 as sqlite
import datetime
import re


# def get_last_info(hostname):
# 	con = sqlite.connect('local/sys.db')
# 	cur = con.cursor()
# 	# res = cur.execute("SELECT * FROM infosys;").fetchall()
# 	res = cur.execute("SELECT * FROM infosys WHERE hostname = :hostname ORDER BY date DESC LIMIT 1;", {'hostname': '	biel'}).fetchone()

# 	info = {}
# 	info['date'] = res[0]
# 	info['hostname'] = res[1]
# 	info['processes'] = res[2]
# 	info['users'] = res[3]
# 	info['cpu'] = res[4]
# 	info['ram'] = res[5]
# 	info['disk'] = res[6]
# 	info['swap'] = res[7]
# 	return info


def get_last_date(hostname):
	""" description """
	con = sqlite.connect('local/sys.db')
	cur = con.cursor()
	return cur.execute("SELECT * FROM infosys WHERE hostname = :hostname ORDER BY date DESC LIMIT 1;", {'hostname': hostname}).fetchone()[0]


def have_sent_request(hostname, now, delta):
	last_date = get_last_date(hostname)
	last_date = re.sub(':', ' ', re.sub('-', ' ', last_date))
	last_date = datetime.datetime.strptime(last_date, '%Y %m %d %H %M %S')
	con = sqlite.connect('local/sys.db')
	cur = con.cursor()
	min = now - datetime.timedelta(days=delta['day'], hours=delta['hour'], minutes=delta['minutes'], seconds=delta['sec'])
	return last_date > min


now = datetime.datetime.now()
delta = {}
delta['day'] = 0
delta['hour'] = 2
delta['minutes'] = 30
delta['sec'] = 0
verif = have_sent_request('biel', now, delta)
# print verif

# for i in res:
# 	print i
# con.close()
# cur.execute("ALTER TABLE infosys ADD COLUMN swap double")
# cur.commit()
# cur.execute("UPDATE infosys SET date = '2017-3-8' WHERE nbProcessus = 219;")
# con.commit()
