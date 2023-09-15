import sqlite3

cmd = 'SELECT * FROM INFORMATION_SCHEMA.TABLES'

DB_NAME = "../db.sqlite3"


def execute(command):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute(command)
    fetch = cur.fetchall()
    con.commit()
    con.close()
    return fetch


print(execute(cmd))