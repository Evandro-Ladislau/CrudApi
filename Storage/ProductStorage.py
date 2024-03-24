import sqlite3
from Model.Product import Product

class ProductStorage:
    def __init__ (self):
        self.conn = sqlite3.connect("Store", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), description VARCHAR(255),price DECIMAL(10,2))")
    
    def create_table(self, sql):
        self.cursor.execute(sql) 
    
    def insert(self, Product):
        query = "INSERT INTO products (id, name, description, price) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (Product.id, Product.name, Product.description, Product.price))
        self.conn.commit()
    
    def select(self):
        try:
            query = "SELECT id, name, price FROM products ORDER BY name"
            response = self.cursor.execute(query)
            data = response.fetchall()
            return data
        except sqlite3.Error as e:
            error_message = f"Error updating product: {e}"
        return {"error": error_message}, 500
           
    def select_by_id(self, id):
        query = "SELECT id, name, description, price FROM products WHERE id=?"
        response = self.cursor.execute(query, (id,))
        data = response.fetchone()
        if data:
            product = Product(id=data[0], name=data[1], description=data[2], price=data[3])  
            return product
        else:
            return False
    
    def update(self, id, price):
        try:
            query = "UPDATE products SET price=? WHERE id=?"
            self.cursor.execute(query, (price, id, ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating product: {e}")
            return False         
    
    def delete_by_id(self, id):
        try:
            query = "DELETE FROM products WHERE id=?"    
            self.cursor.execute(query, (id,))
            rows_deleted = self.cursor.rowcount
            self.conn.commit()
            
            if rows_deleted == 0:
                print("Product with given ID does not exist.")
                return False
            else:
                print("Product deleted successfully.")
                return True
        except sqlite3.Error as e:
            print(f"SQLite error deleting product: {e}")
            return False    