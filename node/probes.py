#!/usr/bin/python
#-*- coding: utf-8 -*-

# Récupère les informations systèmes

import psutil
import socket
import subprocess
import os


def get_system_information():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    infos = {}
    infos['hostname']  = socket.gethostname()
    infos['processes'] = len(psutil.pids())
    infos['users']     = os.popen('users | wc -w') # sonde mixte
    infos['cpu']       = os.popen('{}/get_cpu.sh'.format(dir_path)) # sonde bash
    infos['cpu']       = psutil.cpu_percent()
    infos['ram']       = psutil.virtual_memory()[2]
    infos['disk']      = psutil.disk_usage('/')[3]
    infos['swap']      = psutil.swap_memory()[2]
    return infos
