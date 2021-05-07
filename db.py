import sqlite3 as sl
import os.path


class dbms:
    def __init__(self):
        if os.path.isfile('primary.db') == False:
            self.con = sl.connect('primary.db')

            with self.con:
                self.con.execute("""
                    CREATE TABLE SETTINGS (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    param TEXT,
                    type TEXT
                    );
                """)
        else:
            self.con = sl.connect('primary.db')


    def insertToSettings(self, data):
        sql = 'INSERT INTO SETTINGS (name, param, type) values(?, ?, ?)'
        with self.con:
            self.con.executemany(sql, data)

    def getFromSettings(self, field, value):
        with self.con:
            data = self.con.execute("SELECT * FROM SETTINGS WHERE "+ field +" == '" + value + "'")
            return data.fetchall()

    def getEverythingFromSettings(self):
        with self.con:
            data = self.con.execute("SELECT * FROM SETTINGS")
            return data.fetchall()

    def updateSettings(self, identifier, data):
        sql = "UPDATE SETTINGS SET name = ? , param = ? , type = ? WHERE " + identifier + " = ?"
        cur = self.con.cursor()
        cur.execute(sql, data)
        self.con.commit()
        
    def deleteFromSettings(self, id):    
        sql = 'DELETE FROM SETTINGS WHERE id=?'
        cur = self.con.cursor()
        cur.execute(sql, (id,))
        self.con.commit()
    
#for i in dbms().getEverythingFromSettings():
    #print(i)