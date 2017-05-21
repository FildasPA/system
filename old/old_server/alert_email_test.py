#!/usr/bin/python
#-*- coding: utf-8 -*-

import smtplib

envoi = 'albacristo30.gmail.com'						#Expéditeur de l'email
destination = 'albacristo30@gmail.com'					#Destinataire de l'email

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)			#Connexion au serveur SMTP
#server.starttls()										#Connexion a GMAIL
server.ehlo()
server.login('albacristo30.gmail.com', 'mdp')	#Identification

mess = "Un problème a été rencontré ! "					#Message suivant le problème
server.sendmail(envoi, destination, mess)				#Envoi du message de l'expéditeur vers le destinataire
server.quit()											#Déconnexion du serveur
