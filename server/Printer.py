#!/usr/bin/python
#-*- coding: utf-8 -*-


def get_last_info(hostname):
	con = sqlite.connect(Config.DB_FILE)
	cur = con.cursor()
	res = cur.execute("SELECT * FROM infosys WHERE hostname = :hostname ORDER BY date DESC LIMIT 1;", {hostname: 'biel'}).fetchone()

	info = {}
	info['date'] = res[0]
	info['hostname'] = res[1]
	info['processes'] = res[2]
	info['users'] = res[3]
	info['cpu'] = res[4]
	info['ram'] = res[5]
	info['disk'] = res[6]
	info['swap'] = res[7]

	return info


def get_hostnames():
    con = sqlite.connect(Config.DB_FILE)
    cur = con.cursor()
    return cur.execute("SELECT DISTINCT(hostname) FROM infosys ORDER BY hostname;").fetchall()
