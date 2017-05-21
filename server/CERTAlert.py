#!/usr/bin/python
#-*- coding: utf-8 -*-

# Affiche la dernière alerte du C.E.R.T.

import feedparser
import re
import datetime
import sqlite3 as sqlite
import Config
import utils


def get_max_date():
	con = sqlite.connect(Config.DB_FILE)
	cur = con.cursor()
	return cur.execute("SELECT MAX(date) FROM certalert;").fetchone()[0]


def save_entry(date, entry_title):
	con = sqlite.connect(Config.DB_FILE)
	cur = con.cursor()
	cur.execute("INSERT INTO certalert (date, title) VALUES (:date, :title);", {'date': now, 'title': entry_title})
	con.commit()


def get_last_alert():
	feed = feedparser.parse('http://www.cert.ssi.gouv.fr/site/cert-fr_alerte.rss')
	if not feed.entries:
		print "No entry. No connection ?"
		exit(1)
	return feed.entries[0].title


if __name__ == '__main__':
	entry_title = get_last_alert()
	max_date = get_max_date()
	now = datetime.datetime.now()
	print now
	# if max_date == None:
	# 	save_entry(now, entry_title)
	# else:
	# 	max_date = re.sub(':', ' ', re.sub('-', ' ', max_date))
 #        max_date = datetime.datetime.strptime(max_date, '%Y %m %d %H %M %S')
 #        if now > max_date:
	# 		save_entry(date, entry_title)
