#!/usr/bin/python
#-*- coding: utf-8 -*-

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

    @staticmethod
    def color(msg, color):
        return color + str(msg) + Colors.RESET
