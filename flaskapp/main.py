from flask import Flask, jsonify, request
from service_layer import my_service

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_www():
    return jsonify("Hello World from local :DD")


@app.route("/api/v1/whoareyou", methods=['POST'])
def how_are_you():
    entry_data = request.get_json()
    response_data = {
        'name': my_service.get_random_entry()
    }

    return jsonify(response_data)


if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=8080)
      # export PYTHONPATH=$(pwd)
