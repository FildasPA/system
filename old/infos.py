#!/usr/bin/python
#-*- coding: utf-8 -*-

# Affiche les informations sur la machine

import psutil
import socket
import ConfigParser
import re

class Colors:
    PURPLE    = ''
    BLUE      = ''
    GREEN     = ''
    YELLOW    = ''
    RED       = ''
    RESET     = ''
    BOLD      = ''
    UNDERLINE = ''

    @staticmethod
    def activate():
        Colors.PURPLE    = '\033[95m'
        Colors.BLUE      = '\033[94m'
        Colors.GREEN     = '\033[92m'
        Colors.YELLOW    = '\033[93m'
        Colors.RED       = '\033[91m'
        Colors.RESET     = '\033[0m'
        Colors.BOLD      = '\033[1m'
        Colors.UNDERLINE = '\033[4m'

def printinfo(msg, info):
    print str(msg) + color(info, Colors.GREEN)

def color(msg, color):
    return color + str(msg) + Colors.RESET

def print_err(msg):
    print color("Erreur: ", Colors.RED) + str(msg)

def print_warning(msg):
    print color("Attention: ", Colors.YELLOW) + str(msg)

def get_system_informations():
    infos = {}
    infos['hostname']     = socket.gethostname()
    infos['processes']    = len(psutil.pids())
    infos['users']        = len(psutil.users())
    memory                = psutil.swap_memory()
    infos['ram']          = memory[3]
    infos['totalmem']     = memory[0] / 1000000000
    infos['usedmem']      = memory[1] / 1000000000
    infos['availablemem'] = memory[2] / 1000000000
    infos['diskusage']    = psutil.disk_usage('/')[3]
    infos['disks']        = len(psutil.disk_partitions())
    return infos

def print_informations(infos):
    config = ConfigParser.ConfigParser()
    config.read('./config/infos.conf')
    for section in config.sections():
        for option in config.items(section):
            info = re.sub('"','',option[1].strip())
            value = infos[option[0]]
            print '{0:<35} {1:>7}'.format(info, color(value, Colors.GREEN))

    # for nom, info in infos.items():


        # print '%-15s %s' % (nom, info)

    # assume that your data rows are tuples
    # template = "{0:8}|{1:10}|{2:15}|{3:7}|{4:10}" # column widths: 8, 10, 15, 7, 10
    # print template.format("CLASSID", "DEPT", "COURSE NUMBER", "AREA", "TITLE") # header
    # for rec in your_data_source:
    # print template.format(*rec)
    # for rec in your_data_source:

    # print template.format("Nombre de processus lances ", processes)
    # print template.format("Nombre d'utilisateur connectés ", users)
    # print template.format("Machine",hostname)
    # print template.format("Machine",hostname)
    # print template.format("Machine",hostname)
    # print template.format("Machine",hostname)

    # printinfo("Machine                        : ", hostname)
    # printinfo("Nombre de processus lances     : ", processes)
    # printinfo("Nombre d'utilisateur connectés : ", users)
    # printinfo("RAM utilisée (%)               : ", ram)
    # printinfo("Memoire disque restante (%)    : ", diskusage)
    # printinfo("Nombre de disques              : ", disks)
    # printinfo("Memoire utilisee (%)           : ", usedmem)
    # print "Memoire totale en GB           : ", totalmem
    # print "Memoire disponible en GB       : ", availablemem
    # print "Disques: "
    # for disk in psutil.disk_partitions():
    # 	print "  ", disk[0]

infos = get_system_informations()

Colors.activate()
print_informations(infos)
# template = "{0:8} : {1:10}" # column widths: 8, 10, 15, 7, 10


# parser = argparse.ArgumentParser(description=DESCRIPTION,
#                                  formatter_class=RawTextHelpFormatter)
#     parser.add_argument('evaluated_file',
#                         help="Specify the file to evaluate")
#     parser.add_argument('reference_file',
#                         help="Specify the reference file")
#     parser.add_argument('-c', '--color', action="store_true", default=False,
#                         help="Print colors")
#     parser.add_argument('-m', '--matching-cuts', action="store_true", default=False,
#                         help="Only prints phrases with matching cut")
#     parser.add_argument('-u', '--unmatched', action="store_true", default=False,
#                         help="Prints phrases with unmatched cuts (from both files)")
#     parser.add_argument('-v', '--verbose', action="store_true", default=False,
#                         help="Display statistics and phrases with matching cut")
#     parser.add_argument('-w', '--words', type=int,
#                         help="Define the number of words to print; 0 will print full sentences")

#     args = vars(parser.parse_args())

#     if args['verbose']:
#         verbose = True


# import sqlite3 as lite

# con = lite.connect('BDD.db')

# with con:
	# cur = con.cursor()
	# cur.execute("drop table infosys")
	# cur.execute("CREATE TABLE infosys (nomMachine text, date datetime, nbUsers int, utilisation double, memoireTotal int, memoireUtilise int, memoireDispo int, nombreDisk int, nomDisk text, utilisationRacine double, nbProcessus int, PRIMARY KEY (nomMachine, date));")
	# cur.execute("INSERT INTO infosys (nomMachine, date, nbUsers, utilisation, memoireTotal, memoireUtilise, memoireDispo, nombreDisk, nomDisk, utilisationRacine, nbProcessus) VALUES(:hostname,:ilest,:nbusers,:mem,:totmem,:usedmem,:availmem,:nbdisk,:nomsDisk,:disque,:nbpids)", {hostname: hostname, ilest: ilest, nbusers: nbusers, mem: mem, totmem: totmem, usedmem: usedmem, availmem: availmem, nbdisk: nbdisk, nomsDisk: nomsDisk, disque: disque, nbpids: nbpids})
	# hostname = 'biel'
	# cur.execute("INSERT INTO infosys (nomMachine) VALUES(:hostname)", {'hostname': hostname})

	# month =

	# SELECT date, nbUsers, utilisation, memoireUtilise, nombreDisk, utilisationRacine, nbProcessus FROM infosys WHERE date > month;
