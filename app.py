from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User

@app.route("/")
def home():
    return "hello world"


@app.route("/signup", methods=["POST"])
def signup():
    new_user = {
        "email": request.form['email'],
        "username": request.form['username'],
        "password": request.form['password']
    }
    user = User(request.form['email'], request.form['username'],  request.form['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(new_user)


app.run(port=4000)
