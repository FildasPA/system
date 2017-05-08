#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
sys.path.append('/home/fildas/rddtool-1.4.3/')

import rrdtool
import tempfile
rrdtool.create('/tmp/test.rrd', 'DS:foo:GAUGE:20:0:U')

DAY = 86400
YEAR = 365 * DAY
fd, path = tempfile.mkstemp('.png')

rrdtool.graph(path,
              '--imgformat', 'PNG',
              '--width', '540',
              '--height', '100',
              '--start', "-%i" % YEAR,
              '--end', "-1",
              '--vertical-label', 'Downloads/Day',
              '--title', 'Annual downloads',
              '--lower-limit', '0',
              'DEF:downloads=downloads.rrd:downloads:AVERAGE',
              'AREA:downloads#990033:Downloads')

info = rrdtool.info('downloads.rrd')
print info['last_update']
print info['ds[downloads].minimal_heartbeat']
