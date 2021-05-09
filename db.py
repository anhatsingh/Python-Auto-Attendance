import sqlite3 as sl
import os.path


class dbms:
    def __init__(self):
        self.con = sl.connect('mainDb.db')
        if os.path.isfile('mainDb.db') == False:
            self.createSettings()
            self.createUnique()

    def createSettings(self):        
        with self.con:
            self.con.execute("""
                CREATE TABLE SETTINGS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                param TEXT,
                type TEXT
                );
            """)
    
    def createUnique(self):
        with self.con:
            self.con.execute("""
                CREATE TABLE UNIQUE_DATA (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                roll_no TEXT,
                full_name TEXT,
                unique_key TEXT
                );
            """)

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




    def insertToUnique(self, data):
        sql = 'INSERT INTO UNIQUE_DATA (roll_no, full_name, unique_key) values(?, ?, ?)'
        with self.con:
            self.con.executemany(sql, data)

    def getFromUnique(self, field, value):
        with self.con:
            data = self.con.execute("SELECT * FROM UNIQUE_DATA WHERE "+ field +" == '" + value + "'")
            return data.fetchall()

    def getEverythingFromUnique(self):
        with self.con:
            data = self.con.execute("SELECT * FROM UNIQUE_DATA")
            return data.fetchall()

    def updateUnique(self, identifier, data):
        sql = "UPDATE UNIQUE_DATA SET roll_no = ? , full_name = ? , unique_key = ? WHERE " + identifier + " = ?"
        cur = self.con.cursor()
        cur.execute(sql, data)
        self.con.commit()
        
    def deleteFromUnique(self, id):    
        sql = 'DELETE FROM UNIQUE_DATA WHERE id=?'
        cur = self.con.cursor()
        cur.execute(sql, (id,))
        self.con.commit()