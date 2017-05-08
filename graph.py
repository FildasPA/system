#!/usr/bin/python
#-*- coding: utf-8 -*-

# Créer les graphes

import pygal

bar_chart = pygal.Line()
bar_chart.title = "Utilisation des ressources en fonction du temps"
bar_chart.y_labels = map(int, range(0, 110, 10))
bar_chart.add('RAM', [20, 40, 10, 92, 50, 10])
bar_chart.add('CPU', [10, 30, 60, 0, 40, 20])
bar_chart.add('Disk', [30, 10, 40, 70, 60, 0])
bar_chart.render_to_file('bar_chart.svg')
