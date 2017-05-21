#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import os.path
import smtplib
import Config


def send_mails(crises):
	config = Config.config
	for section in config.sections():
		if 'Mail' in section:
			send_mail(section, crises)


def send_mail(section, crises):
	config = Config.config

	# Connexion au serveur SMTP
	server = smtplib.SMTP_SSL(config.get(section, 'smtp'), config.get(section, 'port'))
	# Connexion
	server.ehlo()
	# Identification
	server.login(config.get(section, 'sender'), config.get(section, 'password'))

	crises_messages = ''
	for key, value in crises.iteritems():
		crises_messages += "{} : {}\n".format(key, value)
	message = config.get(section, 'message') + crises_messages
	# Envoi du message de l'expéditeur vers le destinataire
	server.sendmail(config.get(section, 'sender'), config.get(section, 'receiver'), message)
	# Déconnexion
	server.quit()

send_mails({"processes":"250"})
