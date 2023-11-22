from main import sessionids
from db import db

from sqlalchemy.exc import IntegrityError
from methods.user.login.password.calculate_hash import calculateHash
import methods.user.login.query.user as user
from methods.user.login.password.verify_password import verify_username_password
import methods.user.pki.pki_interface as pki_interface


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
            # Creates the object
            x = sessionids(userid = target_user._id)

            # Session ID hashing
            SESSIONID = x.sessionid
            x.sessionid = str(calculateHash(x.sessionid.encode()))

            # Generate the Public and Private Keys
            PUBLIC_KEY, PRIVATE_KEY = pki_interface.get_key_pairs(password)
            x.public_key = PUBLIC_KEY

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
                "sessionid": SESSIONID,
                "private_key": PRIVATE_KEY.decode(encoding="utf-8")
            }}
    else:
        return {"success": False, "response": "User not found!", "data": {}}