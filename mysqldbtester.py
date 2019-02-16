import MySQLdb

db = MySQLdb.connect(host="34.207.179.27",
                     port=3306,
                     user="joseph",
                     passwd="josephiscool",
                     db="c_debeautify")

cur = db.cursor()

cur.execute('SELECT * FROM comments')

for row in cur.fetchall():
    print(row[1])

db.close()
