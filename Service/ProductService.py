from Model.Product import Product
from Storage.ProductStorage import ProductStorage

class ProductService:
    def __init__(self):
        self.conn = ProductStorage()
    
    def validate_insert_product(self, Product):
       if not Product.id or not Product.name or not Product.description or Product.price <= 0:
           raise ValueError("Uma ou mais dado do produto invalido!")
       else:
           self.conn.insert(Product)
           
    def select_product(self, id):
        return self.conn.select_by_id(id)
    
    def select_products(self):
        return self.conn.select()
    
    def validate_update_product(self, id, price):
        if price <= 0:
            raise ValueError("Valor inválido")
        else:
            return self.conn.update(id, price)
    
    def delete_product(self, id):
        success = self.conn.delete_by_id(id)
        return success