from flask import Flask, jsonify, request
import product.service

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_www():
    return jsonify("Hello from GCP")


@app.route("/api/products/products", methods=['GET'])
def get_products():
    pass



if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=8080)
      # export PYTHONPATH=$(pwd)
