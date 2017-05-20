#!/usr/bin/python
# coding: utf-8

import psutil
import socket


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
