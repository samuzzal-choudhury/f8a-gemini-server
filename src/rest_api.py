import flask
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/readiness')
def readiness():
    return flask.jsonify({}), 200


@app.route('/api/v1/liveness')
def liveness():
    return flask.jsonify({}), 200


@app.route('/api/v1/scan', methods=['POST'])
def scan():
    input_json = request.get_json()
    r = {}
    return flask.jsonify({}), status


@app.route('/api/v1/register', methods=['POST'])
def register():
    input_json = request.get_json()
    return flask.jsonify({}), status


@app.route('/api/v1/report/<repo>')
def report(repo):
    return flask.jsonify({})


if __name__ == "__main__":
    app.run()
