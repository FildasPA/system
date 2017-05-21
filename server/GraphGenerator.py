#!/usr/bin/python
#-*- coding: utf-8 -*-

# Génère un graphe représentant l'utilisation des ressources d'une marchine donnée en fonction du temps

import pygal
import re
from datetime import datetime
import sqlite3 as sqlite
import Config


def get_info(hostname, start, end):
    """Récupère les infos de la bdd, les formate, les ajoute
    dans un dictionnaire de listes avant de le retourner"""
    con = sqlite.connect(Config.CONFIG_FILE)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM infosys WHERE (hostname = :hostname AND date >= :start AND date < :end) ORDER BY date;", {'hostname': hostname, 'start': start, 'end': end}).fetchall()

    info              = {}
    info['dates']     = []
    info['processes'] = []
    info['users']     = []
    info['cpu']       = []
    info['ram']       = []
    info['disk']      = []
    info['swap']      = []

    for i in res:
        d = re.sub(':', ' ', re.sub('-', ' ', i[0]))
        date = datetime.strptime(d, '%Y %m %d %H %M %S')
        info['dates'].append(date)
        info['processes'].append(i[2])
        info['users'].append(i[3])
        info['cpu'].append(i[4])
        info['ram'].append(i[5])
        info['disk'].append(i[6])
        info['swap'].append(i[7])

    return info


def generate_graph(filename, hostname, info, categories):
    datetimeline  = pygal.DateTimeLine(x_label_rotation=35, title=hostname)

    for category in categories:
        if category in info:
            i = [(date, i) for date, i in zip(info['dates'], info[category])]
            datetimeline.add(category, i)

    datetimeline.render_to_file(filename)


if __name__ == '__main__':
    hostname = 'biel'
    start = "{year}-{month}-{day} {hour}:{minutes}:{sec}".format(year=2017, month=5, day=20, hour=16, minutes=44, sec=00)
    end = "{year}-{month}-{day} {hour}:{minutes}:{sec}".format(year=2017, month=5, day=20, hour=16, minutes=45, sec=28)

    info = get_info(hostname, start, end)
    if not info:
        exit(1)

    filename = '{}_{}-{}_p.svg'.format(hostname, info['dates'][0], info['dates'][-1])
    generate_graph(filename, hostname, info, ['cpu','ram','disk','swap'])
    filename = '{}_{}-{}.svg'.format(hostname, info['dates'][0], info['dates'][-1])
    generate_graph(filename, hostname, info, ['processes','users'])
