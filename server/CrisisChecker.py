#!/usr/bin/python
#-*- coding: utf-8 -*-

import os.path
import ConfigParser
import Config
import read_config

SECTION = 'Crisis'


def add_section(config):
    config.add_section(SECTION)
    config.set(SECTION, "no_response", "30")
    config.set(SECTION, "cpu", "90")
    config.set(SECTION, "ram", "100")
    config.set(SECTION, "disk", "95")


def get_crises(info):
    """Return crises"""
    config = Config.config
    read_config.check_section_exists(config, SECTION, lambda: add_section())
    crises = {}

    # for option in config.items(SECTION):
    #     if option[0] in info:
    #         if float(info[option[0]]) >= float(option[1]):
    #             crises[option[0]] = info[option[0]]

    return crises


# def get_last_response(hostname):


# def check_last_response(hostname):
#     config = read_config()
#     max_no_response = config.get(SECTION, 'no_response')
#     last_response = get_last_response(hostname)
    # if(last_response > )


# if __name__ == "__main__":
#     check_response()
