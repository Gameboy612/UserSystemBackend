from methods.user.login.session.get_session_id import login as getSessionID
from methods.user.login.password.change_password import getSaltAndHash
from main import users, sessionids, db

from sqlalchemy.exc import IntegrityError

def register(username: str, password: str, users: users, sessionids: sessionids, db: db) -> dict:
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
                    password=password,
                    users=users,
                    sessionids=sessionids,
                    db=db
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