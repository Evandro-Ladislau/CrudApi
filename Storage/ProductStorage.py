import sqlite3

class ProductStorage:
    
    def __init__ (self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.createTable("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), description VARCHAR(255),price DECIMAL(10,2))")
    
    def createTable(self, sql):
        self.cursor.execute(sql)
        
    def verifyTable(self):
        res = self.cursor.execute("SELECT name FROM sqlite_master")
        print(res.fetchone())    
            