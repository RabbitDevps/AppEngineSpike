from flask import Flask, jsonify, request

import product.service as product_service

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_www():
    return jsonify("Hello from GCP")


# ######################################################################################################################
#                                               PRODUCTS
# ######################################################################################################################


@app.route("/api/products/products", methods=['GET'])
def get_products():
    products = product_service.get_products()
    products_json = [product.__dict__ for product in products]
    if products_json:
        return jsonify(products_json)
    return 'Not Found', 404


@app.route("/api/products/products", methods=['POST'])
def create_product():
    data = request.json
    product_service.create_product(data)
    return "Created", 201


@app.route("/api/products/products/<product_id>", methods=['GET'])
def get_product(product_id):
    products = product_service.get_product(product_id)
    products_json = [product.__dict__ for product in products]
    if products_json:
        return jsonify(products_json)
    return 'Not Found', 404


@app.route("/api/products/products/<product_id>", methods=['DELETE'])
def delete_product(product_id):
    response = product_service.delete_product(product_id)
    if response:
        return 'OK', 200
    return 'Not Found', 404


# ######################################################################################################################


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    # export PYTHONPATH=$(pwd)
