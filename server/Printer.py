#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import ConfigParser
import argparse


def get_last_info(hostname):
	con = sqlite.connect(Config.DB_FILE)
	cur = con.cursor()
	res = cur.execute("SELECT * FROM infosys WHERE hostname = :hostname ORDER BY date DESC LIMIT 1;", {hostname: 'biel'}).fetchone()

	info = {}
	info['date'] = res[0]
	info['hostname'] = res[1]
	info['processes'] = res[2]
	info['users'] = res[3]
	info['cpu'] = res[4]
	info['ram'] = res[5]
	info['disk'] = res[6]
	info['swap'] = res[7]

	return info


def get_hostnames():
    con = sqlite.connect(Config.DB_FILE)
    cur = con.cursor()
    return cur.execute("SELECT DISTINCT(hostname) FROM infosys ORDER BY hostname;").fetchall()


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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-p', '--porcelain', action="store_true", default=False,
                        help="Formate la sortie pour être facilement utilisée par un script")
    parser.add_argument('-c', '--color', action="store_true", default=False,
                        help="Affiche des couleurs")
    parser.add_argument('-p', '--porcelain', action="store_true", default=False,
                        help="Formate la sortie pour être facilement utilisée par un script")
    args = vars(parser.parse_args())

    # if args['color']:
        # Colors.activate()

