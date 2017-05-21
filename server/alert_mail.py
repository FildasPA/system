#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read('sys.conf')

envoi = cfg.get('Mail1','sender')						#Expéditeur de l'email
destination = cfg.get('Mail1','receiver')					#Destinataire de l'email
smtpserver = cfg.get('Mail1','smtp')
port = cfg.get('Mail1','port')
mdp = cfg.get('Mail1','password')
mess = cfg.get('Mail1','message')


def send_mail(s,crise):
	server = smtplib.SMTP_SSL(s['smtp'], s['port'])					#Connexion au serveur SMTP
	server.ehlo()									#Connexion
	server.login(s['sender'], s['password'])							#Identification
	
	crises = ''
	for key, value in crise:
		crises += "{} la valeur n'est pas conforme {}\n".format(key, value)"
	message = s['message'] + crises
	server.sendmail(s['sender'], s['receiver'], message)					#Envoi du message de l'expéditeur vers le destinataire
	server.quit()									#Déconnexion du serveur

#mess = "Une situation de crise a ete rencontree ! "				#Message suivant le problème

#Pour la configuration du mail, utiliser send_mail.py pour créer le fichier config et les informations sont:
#title pour le titre de la config du mail (exemple université ou gmail etc)
#sender pour l'expéditeur
#password pour le mot de passe
#receiver pour le destinataire du mail
#smtp pour l'adresse du serveur smtp
#port pour le port par lequel passe le seveur smtp
#message pour le message qui sera affiché
