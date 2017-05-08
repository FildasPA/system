#!/usr/bin/python
#-*- coding: utf-8 -*-

# Affiche la dernière alerte du C.E.R.T.

import feedparser

feed = feedparser.parse('http://www.cert.ssi.gouv.fr/site/cert-fr_alerte.rss')

if not feed.entries:
	print "No entry. No connection ?"
	exit(1)

print feed.entries[0].title
