#!/usr/bin/python
#-*- coding: utf-8 -*-

import os.path
import ConfigParser
import Config
import read_config

SECTION = 'Crisis'


def get_crises(info):
    """Return crises"""
    config = Config.config

    crises = {}
    for option in config.items(SECTION):
        if option[0] in info:
            if float(info[option[0]]) >= float(option[1]):
                crises[option[0]] = info[option[0]]

    return crises


def get_last_date(hostname):
    """ description """
    con = sqlite.connect('local/sys.db')
    cur = con.cursor()
    return cur.execute("SELECT * FROM infosys WHERE hostname = :hostname ORDER BY date DESC LIMIT 1;", {'hostname': hostname}).fetchone()[0]


def have_sent_request(hostname, now, delta):
    last_date = get_last_date(hostname)
    last_date = re.sub(':', ' ', re.sub('-', ' ', last_date))
    last_date = datetime.datetime.strptime(last_date, '%Y %m %d %H %M %S')
    con = sqlite.connect('local/sys.db')
    cur = con.cursor()
    min = now - datetime.timedelta(days=delta['day'], hours=delta['hour'], minutes=delta['minutes'], seconds=delta['sec'])
    return last_date > min


now = datetime.datetime.now()
delta = {}
delta['day'] = 0
delta['hour'] = 2
delta['minutes'] = 30
delta['sec'] = 0
verif = have_sent_request('biel', now, delta)

# def get_last_response(hostname):


# def check_last_response(hostname):
#     config = read_config()
#     max_no_response = config.get(SECTION, 'no_response')
#     last_response = get_last_response(hostname)
    # if(last_response > )


# if __name__ == "__main__":
#     check_response()
print(get_crises({'cpu': 95, 'ram': 50}))
