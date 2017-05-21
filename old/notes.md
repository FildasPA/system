# Notes

## SQLite

con = lite.connect('BDD.db')
cur = con.cursor()
cur.execute("UPDATE infosys SET date = '2017-3-8' WHERE nbProcessus = 219;")
con.commit()
cur.execute("SELECT * FROM infosys;").fetchall()
con.close()


## Cron

0 0 0 1 0 python refresh.py
