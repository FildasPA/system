#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import os.path
import smtplib

#Pour la configuration du mail, utiliser send_mail pour créer le fichier config et les informations sont:
#title pour le titre de la config du mail (exemple université ou gmail etc)
#sender pour l'expéditeur
#password pour le mot de passe
#receiver pour le destinataire du mail
#smtp pour l'adresse du serveur smtp
#port pour le port par lequel passe le seveur smtp
#message pour le message qui sera affiché

#Exemple pour GMAIL
#title = GMAIL
#sender = L3avignonessai@gmail.com
#password = 
#receiver = L3avignonessai@gmail.com
#smtp = smtp.gmail.com
#port = 465
#message = Une situation de crise a ete rencontree ! 
 
def write_config_file(filename, config):
    section = 'Mail1'
    config.add_section(section)
    config.set(section, "title", "Université")
    config.set(section, "sender", "")
    config.set(section, "password", "")
    config.set(section, "receiver", "")
    config.set(section, "smtp", "smtpz.univ-avignon.fr")
    config.set(section, "port", "465")
    config.set(section, "message", "Une situation de crise a ete rencontree ! \n Le probleme vient de : \n")
    config.write(open(filename, 'w'))


def read_config():
    """Read config file, or write one if there is none"""
    filename = './local/sys.conf'
    config = ConfigParser.ConfigParser()
    if not os.path.isfile(filename):
        write_config_file(filename, config)
    config.read(filename)
    #for section in config.sections():
    	#if 'Mail' in section:
        #write_config_file(filename, config)
    return config


def print_crise(crise):
    config = read_config()
    for section in config.sections():
		if 'Mail' in section:
			send_mail(config,section,crise)
		
		
def send_mail(config, section, crise):
	print crise
	config.get(section, 'smtp')
	server = smtplib.SMTP_SSL(config.get(section, 'smtp'), config.get(section, 'port'))					#Connexion au serveur SMTP
	server.ehlo()									#Connexion
	server.login(config.get(section, 'sender'), config.get(section, 'password'))							#Identification
	
	crises = ''
	for key, value in crise.iteritems():
		crises += "{} la valeur n'est pas conforme {}\n".format(key, value)
	message = config.get(section, 'message') + crises
	server.sendmail(config.get(section, 'sender'), config.get(section, 'receiver'), message)					#Envoi du message de l'expéditeur vers le destinataire
	server.quit()									#Déconnexion du serveur		


if __name__ == "__main__":
	#read_config()
	print_crise({"processes":"250"})
