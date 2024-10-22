import sqlite3
import os

os.chdir("D:\Python_Egitim\Python_MySQL_SQLite")
conn=sqlite3.connect("chinook.db")
cursor=conn.cursor()
query="SELECT * FROM customers"
cursor.execute(query)
result=cursor.fetchall()
for row in result:
    print(row)

conn.close()