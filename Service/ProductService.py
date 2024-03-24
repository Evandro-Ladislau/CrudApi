from Model.Product import Product
from Storage.ProductStorage import ProductStorage

class ProductService:
    def __init__(self):
        self.conn = ProductStorage()
    
    def validate_insert_product(self, Product):
        success = self.conn.select_by_id(Product.id)
        if success:
            raise ValueError("There is already a product registered with this code!") 
        
        if not Product.id or not Product.name or not Product.description or Product.price <= 0:
            raise ValueError("One or more invalid product details!")
        else:
            self.conn.insert(Product)
           
    def select_product(self, id):
        return self.conn.select_by_id(id)
    
    def select_products(self):
        return self.conn.select()
    
    def validate_update_product(self, id, price):
        response = self.conn.select_by_id(id)
        if response == False:
            raise ValueError("This product does not exist!")
        elif price <= 0 :
            raise ValueError("Value must be greater than zero!")
        else:
            return self.conn.update(id, price)
    
    def delete_product(self, id):
        success = self.conn.delete_by_id(id)
        return success