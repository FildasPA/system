#!/usr/bin/python
#-*- coding: utf-8 -*-

import os.path
import ConfigParser
import Config


def write_config(config):
    config.write(open(Config.CONFIG_FILE, 'w'))


def read_config():
    """Read config file, or write one if there is none.
    Then return config."""
    config = ConfigParser.ConfigParser()
    if not os.path.isfile(Config.CONFIG_FILE):
        write_config(config)
    else:
        config.read(Config.CONFIG_FILE)
    return config


def check_section_exists(config, section, add_section):
    if section not in config.sections():
        config = add_section(config)
        write_config(config)
