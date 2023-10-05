from main import sessionids, db

from sqlalchemy.exc import IntegrityError
import methods.user.login.query.user as user
from methods.user.login.password.verify_password import verify_username_password



def login(username: str, password: str) -> dict:
    target_user = user.findUserByUsername(username)

    if target_user:
        if verify_username_password(username=username, password=password):
            # Create SessionID
            while True:
                x = sessionids(userid = target_user._id)
                db.session.add(x)
                try:
                    db.session.commit()
                    break
                except IntegrityError:
                    db.session.rollback()
            
            sessionid = x.sessionid
            return {
                "success": True,
                "response": "Login Successful!",
                "data": {
                    "sessionid": sessionid
                }}
        else:
            return {"success": False, "response": "Password Incorrect!", "data": {}}
    else:
        return {"success": False, "response": "User not found!", "data": {}}