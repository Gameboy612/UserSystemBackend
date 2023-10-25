from main import sessionids
from db import db

from sqlalchemy.exc import IntegrityError
from methods.user.login.password.calculate_hash import calculateHash
import methods.user.login.query.user as user
from methods.user.login.password.verify_password import verify_username_password



def login(username: str, password: str) -> dict:
    SESSIONID = ""
    target_user = user.findUserByUsername(username)
    if target_user:
        if not verify_username_password(username=username, password=password):
            return {
                    "success": False,
                    "response": "Password Incorrect!",
                    "data": {}
                }
        
        # Create SessionID
        while True:
            x = sessionids(userid = target_user._id)
            SESSIONID = x.sessionid
            x.sessionid = str(calculateHash(x.sessionid.encode()))
            db.session.add(x)
            try:
                db.session.commit()
                break
            except IntegrityError:
                db.session.rollback()
        
        return {
            "success": True,
            "response": "Login Successful!",
            "data": {
                "sessionid": SESSIONID
            }}
    else:
        return {"success": False, "response": "User not found!", "data": {}}