import sys 
sys.path.append(r'C:\Users\Evandro Ladislau\Documents\plataforma\CrudApi')
from Model.Product import Product

class ProductService:
    @staticmethod
    def validateProduct(Product):
       if not Product.id or not Product.name or not Product.description or Product.price <= 0:
           raise ValueError("Uma ou mais dado do produto invalido!")