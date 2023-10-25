from methods.user.login.session.get_session_id import login as getSessionID
from methods.user.login.password.change_password import getSaltAndHash
from methods.user.login.password.secure_password import check_security
from main import users
from db import db

from sqlalchemy.exc import IntegrityError

def register(username: str, password: str) -> dict:
    # Check password secure
    r = check_security(password=password)
    if not r["success"]:
        return r
    


    salt, hash = getSaltAndHash(password)

    user = users(
        username=username,
        hash=hash,
        salt=salt
    )
    # Try to add to users
    db.session.add(user)
    try:
        db.session.commit()
        res = getSessionID(
                    username=username,
                    password=password
                )
        if res["success"]:
            return {
                "success": True,
                "response": "User created!",
                "data": {
                    "sessionid": res["data"]["sessionid"]
                }
            }
        return res
    except IntegrityError:
        db.session.rollback()
        return {
            "success": False,
            "response": "Username is taken.",
            "data": {}
        }