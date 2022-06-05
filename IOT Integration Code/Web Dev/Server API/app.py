from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'file:////Users/smartguy88-home/Desktop/The-WildStar-Project/IOT Integration Code/Web Dev/Server API/data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.create_all()


class ESP32(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<ESP32 id:{id}>"


@app.route("/")
def gg():
    return "<h1>yes daddy I OH!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
