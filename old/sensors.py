#!/usr/bin/python
# coding: utf-8

# Affiche les informations sur la machine

import psutil
import socket
import ConfigParser
import re
import argparse
import os.path
# from utils.colors import *


DESCRIPTION = """
Vous pouvez ajouter dans le fichier de configuration:
- hostname
- separator
- processes
- users
- cpu
- ram
- disk
- swap
"""
SECTION = 'Informations'


def get_system_information():
    infos = {}
    infos['hostname']  = socket.gethostname()
    infos['processes'] = len(psutil.pids())
    infos['users']     = len(psutil.users())
    infos['cpu']       = psutil.cpu_percent()
    infos['ram']       = psutil.virtual_memory()[2]
    infos['disk']      = psutil.disk_usage('/')[3]
    infos['swap']      = psutil.swap_memory()[2]
    return infos


def write_config_file(filename, config):
    config.add_section(SECTION)
    config.set(SECTION, "hostname", "Machine")
    config.set(SECTION, "separator", "  ----------------------------------------------")
    config.set(SECTION, "processes", "Nombre de processus")
    config.set(SECTION, "users", "Nombre d'utilisateurs connectes")
    config.set(SECTION, "cpu", "CPU")
    config.set(SECTION, "ram", "RAM")
    config.set(SECTION, "disk", "Disque")
    config.write(open(filename, 'w'))
    return config


def read_config():
    """Read config file, or write one if there is none"""
    filename = './local/sys.conf'
    config = ConfigParser.ConfigParser()
    if not os.path.isfile(filename):
        write_config_file(filename, config)
    else:
        config.read(filename)
        if SECTION not in config.sections():
            write_config_file(filename, config)
    return config


def print_informations(infos, porcelain):
    config = read_config()
    for option in config.items(SECTION):
        if option[0] == 'separator' and not porcelain:
            print re.sub('"', '', option[1])
            continue
        elif option[0] not in infos:
            continue
        info = re.sub('"', '', option[1].strip())
        value = infos[option[0]]
        if porcelain:
            msg = '{} {}'.format(option[0], value)
        else:
            msg = '{0:<35} '
            msg += '{1:>19}' if Colors.GREEN else '{1:>10}'
            msg = msg.format(info, Colors.color(value, Colors.GREEN))
        print msg


def collect():
    infos = get_system_information()
    print_informations(infos, args['porcelain'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-c', '--color', action="store_true", default=False,
                        help="Affiche des couleurs")
    parser.add_argument('-p', '--porcelain', action="store_true", default=False,
                        help="Formate la sortie pour être facilement utilisée par un script")
    args = vars(parser.parse_args())

    # if args['color']:
        # Colors.activate()

    collect()
