from flask import Flask, request

app = Flask(__name__)


@app.route("/api/v1/dump", methods=["GET"])
def dump():
    ...
