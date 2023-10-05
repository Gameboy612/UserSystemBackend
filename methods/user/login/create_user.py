from methods.user.login.get_session_id import login as getSessionID
from methods.user.login.password.change_password import getSaltAndHash
from main import users, db

from sqlalchemy.exc import IntegrityError

def register(username: str, password: str) -> dict:
    hash, salt = getSaltAndHash(password)

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
        
        return {
            "success": True,
            "response": "User created!",
            "data": {
                "sessionid": res["data"]["sessionid"]
            }
        }
    except IntegrityError:
        db.session.rollback()
        return {
            "success": False,
            "response": "Username is taken.",
            "data": {}
        }