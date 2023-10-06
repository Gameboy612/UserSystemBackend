from main import sessionids, db, users

from sqlalchemy.exc import IntegrityError
import methods.user.login.query.user as user
from methods.user.login.password.verify_password import verify_username_password



def login(username: str, password: str, users: users, sessionids: sessionids, db: db) -> dict:
    target_user = user.findUserByUsername(username, users=users)
    if target_user:
        if not verify_username_password(username=username, password=password, users=users):
            return {
                    "success": False,
                    "response": "Password Incorrect!",
                    "data": {}
                }
        
        # Create SessionID
        while True:
            x = sessionids(userid = target_user._id)
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
                "sessionid": x.sessionid
            }}
    else:
        return {"success": False, "response": "User not found!", "data": {}}