#!/usr/bin/python
#-*- coding: utf-8 -*-

# Affiche les informations sur la machine

import psutil
import socket
import ConfigParser
import re
import argparse
import os.path

DESCRIPTION="""
Vous pouvez ajouter dans le fichier de configuration:
- hostname
- separator
- processes
- users
- cpu
- ram
- diskusage
- swap
"""

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

def color(msg, color):
    return color + str(msg) + Colors.RESET

def get_system_informations():
    infos = {}
    infos['hostname']  = socket.gethostname()
    infos['processes'] = len(psutil.pids())
    infos['users']     = len(psutil.users())
    infos['cpu']       = psutil.cpu_percent()
    infos['ram']       = psutil.virtual_memory()[2]
    infos['disks']     = len(psutil.disk_partitions())
    infos['diskusage'] = psutil.disk_usage('/')[3]
    infos['swap']      = psutil.swap_memory()[2]
    return infos

def write_config_file(filename, config):
    section = 'Informations'
    config.add_section(section)
    config.set(section, "hostname", "Machine")
    config.set(section, "separator", "----------------------------------------------")
    config.set(section, "processes", "Nombre de processus")
    config.set(section, "users","Nombre d'utilisateurs connectes")
    config.set(section, "cpu", "CPU")
    config.set(section, "ram", "RAM")
    config.set(section, "diskusage", "Disque")
    config.write(open(filename,'w'))

def read_config():
    """Read config file, or write one if there is none"""
    filename = './config/infos.conf'

    config = ConfigParser.ConfigParser()

    if not os.path.isfile(filename):
        write_config_file(filename, config)

    config.read(filename)
    return config

def print_informations(infos, porcelain):
    config = read_config()
    for section in config.sections():
        for option in config.items(section):
            if option[0] == 'separator' and not porcelain:
                print re.sub('"','',option[1])
                continue
            elif option[0] not in infos:
                continue
            info = re.sub('"','',option[1].strip())
            value = infos[option[0]]
            if porcelain:
                msg = '{} {}'.format(option[0], value)
            else:
                msg = '{0:<35} '
                if Colors.GREEN:
                    msg += '{1:>19}'
                else:
                    msg += '{1:>10}'
                msg = msg.format(info, color(value, Colors.GREEN))
            print msg


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('-c', '--color', action="store_true", default=False,
                    help="Affiche des couleurs")
parser.add_argument('-p', '--porcelain', action="store_true", default=False,
                    help="Formate la sortie pour être facilement utilisée par un script")
args = vars(parser.parse_args())

if args['color']:
    Colors.activate()

infos = get_system_informations()
print_informations(infos, args['porcelain'])
