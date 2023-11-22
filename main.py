from flask import Flask, request, jsonify
import uuid
import json
import datetime
from traceback import format_exc
from db import db
from methods._utilities.default_responses import METHOD_NOT_FOUND


app = Flask(__name__)
app.secret_key = "svdb"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {
    'profiles': 'sqlite:///profiles.sqlite3',
    'followlinks': 'sqlite:///followlinks.sqlite3',
    'settings': 'sqlite:///settings.sqlite3'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# https://www.reddit.com/r/flask/comments/mbhqnm/use_sqlalchemy_database_from_another_file/
db.init_app(app)

class users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    hash = db.Column(db.String(100))
    salt = db.Column(db.String(29))

    date_created = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, username, hash, salt):
        self.username = username
        self.hash = hash
        self.salt = salt

class sessionids(db.Model):
    __tablename__ = 'sessionids'
    __table_args__ = {'extend_existing': True}
    _id = db.Column("id", db.Integer, primary_key=True)
    sessionid = db.Column(db.String(100), unique=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    public_key = db.Column(db.LargeBinary(451))
    accessedcount = db.Column(db.Integer, default=0)
    lastused = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, userid):
        self.sessionid = str(uuid.uuid4())
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
        try:
            match method[0]:
                case "user":
                    from methods.user._method import run_method
                    if len(method) == 1:
                        return jsonify(METHOD_NOT_FOUND)
                    return run_method(
                        method = method[1:],
                        data = data
                        )
                case "action":
                    from methods.action._method import run_method
                    if len(method) == 1:
                        return jsonify(METHOD_NOT_FOUND)
                    return run_method(
                        method = method[1:],
                        data = data
                    )
        except Exception as e:
            c = uuid.uuid4()
            
            with open(f"errortracker/{c}.txt", "w+", encoding='utf-8') as f:
                f.write(str(datetime.datetime.now()) + "\n")
                f.write(json.dumps(content["method"]))
                f.write("\n\n")
                f.write(format_exc())

            return jsonify({
                "success": False,
                "response": "500 Internal Server Error",
                "data": {
                    "erroruuid": f"{c}"
                }
            })

        return jsonify(METHOD_NOT_FOUND)
    return jsonify({
        "success": False,
        "response": "Incorrect syntax."
    })



if __name__ == "__main__":
    with app.app_context():
        from methods.action.profiles.classes.profiles import profiles
        from methods.action.followlinks.classes.followlinks import followlinks
        from methods.action.settings.classes.privacy_settings import privacy_settings
        from methods.action.settings.classes.profile_viewable_settings import profile_viewable_settings

        db.create_all()
        app.run(host="0.0.0.0", debug=True)