from flask import Flask, request, jsonify
from Model.Product import Product

app = Flask(__name__)

from Controller.ProductController import ProductController
@app.route("/", methods=['GET'])
def list():
    product_controller = ProductController()
    return product_controller.select()

@app.route("/insert", methods=['POST'])
def insert():
    data = request.json
    if data:
        product = Product(id=data.get('id'), name=data.get('name'), description=data.get('description'), price=data.get('price'))
        product_controller = ProductController()
        product_controller.insert(product)
        return jsonify({"message": "Produto inserido com sucesso"}), 201
    else:
        return jsonify({"error": "Dados JSON inválidos"}), 400    

if __name__ == "__main__":
    app.run(debug=True)

