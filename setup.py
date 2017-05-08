import sqlite3 as lite

con = lite.connect('BDD.db')

with con:
	cur = con.cursor()
	cur.execute("CREATE TABLE infosys (nomMachine text, date datetime, nbUsers int, utilisation double, memoireTotal int, memoireUtilise int, memoireDispo int, nombreDisk int, nomDisk text, utilisationRacine double, nbProcessus int, PRIMARY KEY (nomMachine, date));")
	cur.execute("CREATE TABLE cert (date datetime PRIMARY KEY, titre text);")
	cur.execute("CREATE TABLE users (nomMachine text, date datetime, nomUsers text, PRIMARY KEY (nomMachine, date));")
