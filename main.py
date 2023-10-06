from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
import datetime


app = Flask(__name__)
app.secret_key = "svdb"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class users(db.Model):
    __tablename__ = 'users'
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    hash = db.Column(db.String(100))
    salt = db.Column(db.String(29))

    def __init__(self, username, hash, salt):
        self.username = username
        self.hash = hash
        self.salt = salt

class sessionids(db.Model):
    __tablename__ = 'sessionids'
    _id = db.Column("id", db.Integer, primary_key=True)
    sessionid = db.Column(db.Uuid, unique=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    lastused = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, userid):
        self.sessionid = uuid.uuid4()
        self.userid = userid




@app.route("/")
def main():
    return "Please go to /endpoint to submit data"

@app.route("/endpoint", methods=['GET','POST'])
def endpoint():
    # Obtain request
    content = request.json

    if "method" in content and "data" in content:
        data = content["data"]
        method = content["method"].split("/")
        # try:
        match method[0]:
            case "user":
                from methods.user._method import run_method
                return run_method(
                    method = method[1:],
                    data = data,
                    users = users,
                    sessionids = sessionids,
                    db = db
                    )
        # except Exception as e:
        #     return jsonify({
        #         "success": False,
        #         "response": "Exception Occured",
        #         "data": {
        #             "exception": e.args
        #         }
        #     })

        return jsonify({
            "success": False,
            "response": "Method not found."
        })
    return jsonify({
        "success": False,
        "response": "Incorrect syntax."
    })



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)