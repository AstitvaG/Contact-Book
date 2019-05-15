import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE emp (Name TEXT, Email TEXT, MobNo TEXT, City TEXT, Pin TEXT)')
conn.close()