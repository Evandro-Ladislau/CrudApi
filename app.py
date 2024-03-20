from flask import Flask, request, jsonify
from Model.Product import Product
from Service.ProductService import ProductService

app = Flask(__name__)

service = ProductService()

@app.route("/product", methods=['GET'])
def list_products():
    return service.select_products()

@app.route("/product/<int:product_id>", methods=['GET'])
def get_product_by_id(product_id):
    product = service.select_product(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price
            }), 200
    else:
        return jsonify({"error": "Product not exist"}), 400

@app.route("/product", methods=['POST'])
def insert_product():
    data = request.json
    if data:
        product = Product(id=data.get('id'), name=data.get('name'), description=data.get('description'), price=data.get('price'))
        service.validate_insert_product(product)
        return jsonify({"message": "Product inserted successfully"}), 201
    else:
        return jsonify({"error": "Invalid JSON data"}), 400    

@app.route("/product", methods=['PUT'])
def update_product_by_id():
    data = request.json
    if data:
        service.validate_update_product(id=data.get('id'), price=data.get('price'))
        return jsonify({"message": "Product updated successfully"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400 

@app.route("/product/<int:product_id>", methods=['DELETE'])   
def delete_product_by_id(product_id):
    success = service.delete_product(product_id)
    if success:
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete product"}), 500


if __name__ == "__main__":
    app.run(debug=True)

