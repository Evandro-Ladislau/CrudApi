import sqlite3

class ProductFactory:
    
    def __init__ (self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
    
    def createTable(self, sql):
        self.cursor.execute(sql)
        
    def verifyTable(self):
        res = self.cursor.execute("SELECT name FROM sqlite_master")
        print(res.fetchone())    
            