import sqlite3
conn=sqlite3.connect('Mit-Midmorning.db')
print("open database succesfully")
conn.execute("CREATE TABLE Wanfunzi ("
             "ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL TEXT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("tables created succesfully")
conn.close()
