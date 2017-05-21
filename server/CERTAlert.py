#!/usr/bin/python
#-*- coding: utf-8 -*-

# Affiche la dernière alerte du C.E.R.T.

import feedparser
import re
import datetime
import time
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
	print feed['feed']['updated']
	print feed['feed']['updated_parsed']
	return feed.entries[0]


if __name__ == '__main__':
	entry = get_last_alert()
	max_date = get_max_date()
	temps = time.localtime()
	now = "{year}-{month}-{day} {hour}:{minu}:{sec}".format(year=temps.tm_year, month=temps.tm_mon, day=temps.tm_mday, hour=temps.tm_hour, minu=temps.tm_min, sec=temps.tm_sec)

	# print entry['title']

	# La sauvegarde ne fonctionne pas bien (l'entrée est toujours ajoutée, même si elle y est déjà)
	# print "now:      " + str(entry)
	# print "max_date: " + str(max_date)
	# if now > max_date:
	# 	print "save"
	# 	save_entry(now, entry.title)
