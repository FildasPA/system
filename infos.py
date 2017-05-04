#!/usr/bin/python
#-*- coding: utf-8 -*-

import psutil

def get_system_informations():
	""" description """

	users = psutil.users()
	infos_memory = psutil.swap_memory()
	ram          = infos_memory[3]
	totalmem     = infos_memory[0] / 1000000000
	usedmem      = infos_memory[1] / 1000000000
	availablemem = infos_memory[2] / 1000000000

	print "Nombre de processus lances     : ", len(psutil.pids())
	print "Nombre d'utilisateur connectés : ", len(users)
	print "RAM utilisée                   : ", ram
	# print "Memoire totale en GB           : ", totalmem
	print "Memoire utilisee en GB         : ", usedmem
	# print "Memoire disponible en GB       : ", availablemem
	print "Memoire disque restante        : ", psutil.disk_usage('/')[3]
	print "Nombre de disques              : ", len(psutil.disk_partitions())
	# print "Disques: "
	# for disk in psutil.disk_partitions():
	# 	print "  ", disk[0]

# get_system_informations()


import sqlite3 as lite

con = lite.connect('BDD.db')

with con:
	cur = con.cursor()
	# cur.execute("drop table infosys")
	# cur.execute("CREATE TABLE infosys (nomMachine text, date datetime, nbUsers int, utilisation double, memoireTotal int, memoireUtilise int, memoireDispo int, nombreDisk int, nomDisk text, utilisationRacine double, nbProcessus int, PRIMARY KEY (nomMachine, date));")
	# cur.execute("INSERT INTO infosys (nomMachine, date, nbUsers, utilisation, memoireTotal, memoireUtilise, memoireDispo, nombreDisk, nomDisk, utilisationRacine, nbProcessus) VALUES(:hostname,:ilest,:nbusers,:mem,:totmem,:usedmem,:availmem,:nbdisk,:nomsDisk,:disque,:nbpids)", {hostname: hostname, ilest: ilest, nbusers: nbusers, mem: mem, totmem: totmem, usedmem: usedmem, availmem: availmem, nbdisk: nbdisk, nomsDisk: nomsDisk, disque: disque, nbpids: nbpids})
	hostname = 'biel'
	cur.execute("INSERT INTO infosys (nomMachine) VALUES(:hostname)", {'hostname': hostname})

