import sys 
sys.path.append(r'C:\Users\Evandro Ladislau\Documents\plataforma\CrudApi')
import sqlite3
from Storage.ProductStorage import ProductStorage
from Model.Product import Product
from Service.ProductService import ProductService
from flask import Flask

class ProductController:
    def __init__(self):
        self.connectionDB = ProductStorage("Store")
    
    def insert(self,Product):
        query = "INSERT INTO products (id, name, description, price) VALUES (?, ?, ?, ?)"
        ProductService.validateInsertProduct(Product)
        self.connectionDB.cursor.execute(query, (Product.id, Product.name, Product.description, Product.price))
        self.connectionDB.conn.commit()
    
    def select(self):
        query = "SELECT id, name, price FROM products"
        response = self.connectionDB.cursor.execute(query)
        data = response.fetchall()
        for row in data:
            print(row)
    
    def select_by_id(self, id):
        query = "SELECT id, name, price FROM products WHERE id=?"
        response = self.connectionDB.cursor.execute(query, (id,))
        data = response.fetchone()
        return data
    
    def update_by_id(self, id, price):
        ProductService.validateUpdateProduct(price)
        try:
            query = "UPDATE products SET price=? WHERE id=?"
            self.connectionDB.cursor.execute(query, (price, id, ))
            self.connectionDB.conn.commit()
            print("Product update successfully.")
            return True
        except sqlite3.Error as e:
            print(f"Error updating product: {e}")
            return False
        
    def delete_by_id(self, id):
        try:
            query = "DELETE FROM products WHERE id=?"    
            self.connectionDB.cursor.execute(query, (id,))
            rows_deleted = self.connectionDB.cursor.rowcount
            self.connectionDB.conn.commit()
            
            if rows_deleted == 0:
                print("Product with given ID does not exist.")
                return False
            else:
                print("Product deleted successfully.")
                return True
        except sqlite3.Error as e:
            print(f"SQLite error deleting product: {e}")
            return False
            

            
            
controller = ProductController()
#controller.connectionDB.verifyTable()
#telefone = Product(3,'Computer Gamer', 'ADM RYZEN 5500', 3000)
#controller.insertProduct(telefone)
#controller.selectProducts()
controller.delete_by_id(34)





























#import sys
#sys.path.append(r'C:\Users\Evandro Ladislau\Documents\plataforma\CrudApi')
#from Factory import ProductFactory

#crie um instacia da classe Store

#objectStore = ProductFactory("Shopping")

#sql_create_table = "CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), description VARCHAR(255), price DOUBLE(10,2));"
#objectStore.createTable(sql_create_table)

#objectStore.insert("INSERT INTO products VALUES (1,'SrmatPhon Xiaomi', 'Poco X3 GT', 185.00)")
#objectStore.select("SELECT * FROM products")