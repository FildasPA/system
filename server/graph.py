#!/usr/bin/python
#-*- coding: utf-8 -*-

# Créer un graphe représentant l'utilisation des ressources d'une marchine donnée en fonction du temps

import pygal

hostname = "biel"

bar_chart = pygal.Line()
bar_chart.title = "Utilisation des ressources en fonction du temps pour {}".format(hostname)
bar_chart.y_labels = map(int, range(0, 110, 10))
bar_chart.add('RAM', [20, 40, 10, 92, 50, 10])
bar_chart.add('CPU', [10, 30, 60, 40])
bar_chart.add('Disk', [30, 10, 40, 70, 60])
bar_chart.render_to_file('bar_chart.svg')
