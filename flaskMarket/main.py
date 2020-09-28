from flask import Flask, jsonify, request
import pandas as pd


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_www():
    return jsonify("Hello from GCP, Using Pandas test")


@app.route("/api/dataframe", methods=['GET'])
def get_simple_dataframe():
    df = pd.DataFrame({
        'col1': [1,2,3],
        'col2': [4,5,6],
        'col3': [7,8,9],
    })
    return df.to_json()


if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=8080)
      # export PYTHONPATH=$(pwd)
