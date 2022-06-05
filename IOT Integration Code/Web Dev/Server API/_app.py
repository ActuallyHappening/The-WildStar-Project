from crypt import methods
import json
import os
from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

__location__ = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite+pysqlite:////{__location__}/data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class ESP32(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    identifiers = db.Column(db.String(100), nullable=True)  # JSON format
    #hardware = db.Column(db.String(500), nullable=False)
    # JSON/Attatchment format
    attachments = db.Column(db.String(), nullable=True)
    #states = db.relationship("HardwarePinState", backref="board", lazy=False)
    _state = db.Column(db.String(3000), nullable=True)

    def __repr__(self):
        return f"ESP32(id={self.id})"

    def __str__(self):
        return f"<ESP32 id:{self.id}>"


''' class HardwarePinState(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    builtin_state = db.Column(db.String(100), nullable=True)
    total_state = db.Column(db.String(3000), nullable=True)
    board_id = db.Column(db.Integer, db.ForeignKey(
        "esp32.id"), nullable=False) '''


@app.route("/", methods=["GET", "POST"])
def start():
    print(request.method)
    print(request.form['title'])
    if request.form:
        print(f"REQUEST '/' {request.form=}")
    else:
        print(f"ERR? NO {request.form=}")
    return render_template("index.html")


@app.route("/api/v1", methods=["GET", "POST"])
def apiStart():
    print(request.form)
    print(request.args)
    return json.dumps({"__meta__": {"from": "flask API v1", "device": "macOS", "to": ":receiver:", }, })


@app.route("/api/v1/lookup", methods=["GET"])
def apiLookup():
    print(request.args)
    _result = "NO SELECT!"
    if request.args["select"] == "*":
        _result = ESP32.query.all()
        print(_result)
    return str(_result)


@app.route("/api/v1/add", methods=["GET", "POST"])
def apiAdd():
    print(request.args)
    ip = request.args["ip"]
    id = request.args["id"]
    name = request.args["name"]
    esp32 = ESP32(identifiers=json.dumps({"__meta__": {
                  "ctx": "db identifiers"}, "payload": {"IP": ip, "ID": id, "name": name}}))
    db.session.add(esp32)
    db.session.commit()
    return f"Added esp32 {esp32}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969, debug=True)
