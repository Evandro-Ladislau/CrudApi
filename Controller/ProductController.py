import sys 
sys.path.append(r'C:\Users\Evandro Ladislau\Documents\plataforma\CrudApi')
from Factory.ProductFactory import ProductFactory
from Model.Product import Product
from Service.ProductService import ProductService

class ProductController:
    @staticmethod
    def insertProduct(Product):
        connectionDB = ProductFactory("Store")
        query = "INSERT INTO products (id, name, description, price) VALUES (?, ?, ?, ?)"
        ProductService.validateProduct(Product)
        connectionDB.cursor.execute(query, (Product.id, Product.name, Product.description, Product.price))
        connectionDB.conn.commit()
        
    @staticmethod
    def selectProducts():
        connectionDB = ProductFactory("Store")
        query = "SELECT id, name, price FROM products"
        response = connectionDB.cursor.execute(query)
        data = response.fetchall()
        for row in data:
            print(row)
        
#connectiondb = ProductFactory("Store")
#connectiondb.createTable("CREATE TABLE products(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), description VARCHAR(255), price DECIMAL(10,2))")
#connectiondb.verifyTable()

#telefone = Product(3,'Computer Gamer', 'ADM RYZEN 5500', 3000)
#ProductController.insertProduct(telefone)
#ProductController.selectProducts()




























#import sys
#sys.path.append(r'C:\Users\Evandro Ladislau\Documents\plataforma\CrudApi')
#from Factory import ProductFactory

#crie um instacia da classe Store

#objectStore = ProductFactory("Shopping")

#sql_create_table = "CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), description VARCHAR(255), price DOUBLE(10,2));"
#objectStore.createTable(sql_create_table)

#objectStore.insert("INSERT INTO products VALUES (1,'SrmatPhon Xiaomi', 'Poco X3 GT', 185.00)")
#objectStore.select("SELECT * FROM products")