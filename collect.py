#!/usr/bin/python
#-*- coding: utf-8 -*-

# Affiche les informations sur la machine

import psutil
import socket
import ConfigParser
import re
import argparse

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
    infos['hostname']     = socket.gethostname()
    infos['processes']    = len(psutil.pids())
    infos['users']        = len(psutil.users())
    infos['ram']          = psutil.virtual_memory()[2]
    infos['swap']         = psutil.swap_memory()[2]
    infos['diskusage']    = psutil.disk_usage('/')[3]
    infos['disks']        = len(psutil.disk_partitions())
    return infos

def print_informations(infos, porcelain):
    config = ConfigParser.ConfigParser()
    config.read('./config/infos.conf')
    for section in config.sections():
        for option in config.items(section):
            info = re.sub('"','',option[1].strip())
            value = infos[option[0]]
            if porcelain:
                msg = '{} {}'.format(option[0], value)
            else:
                msg = '{0:<35} {1:>7}'.format(info, color(value, Colors.GREEN))
            print msg


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--color', action="store_true", default=False,
                    help="Print colors")
parser.add_argument('-p', '--porcelain', action="store_true", default=False,
                    help="Script format")
args = vars(parser.parse_args())

if args['color']:
    Colors.activate()

infos = get_system_informations()
print_informations(infos, args['porcelain'])
