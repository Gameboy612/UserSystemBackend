import bcrypt

from methods.user.login.query.sessionid import findUserIDBySessionID
from methods.user.login.query.user import findUserByID
from methods.user.login.password.verify_password import verify_userid_password
from methods.user.login.session.remove_session_id import logout_everywhere
from methods.user.login.session.get_session_id import login
from methods.user.login.password.calculate_hash import calculateHash
from methods.user.login.password.secure_password import check_security

from main import users, sessionids, db

def getSaltAndHash(password: str) -> (bytes, str):
    salt = bcrypt.gensalt()
    hash = calculateHash(password=password.encode("utf-8"), salt=salt)
    return salt, hash



def change_password(
        oldpassword: str,
        newpassword: str,
        sessionid: str,
        users: users,
        sessionids: sessionids,
        db: db,
        forcechange: bool = False, ) -> dict:

    r = findUserIDBySessionID(sessionid=sessionid, sessionids=sessionids, db=db)

    if not r["success"]:
        return r

    userid = r["data"]["userid"]

    if not verify_userid_password(userid=userid, password=oldpassword, users=users):
        return {
            "success": False,
            "response": "Incorrect old password.",
            "data": {}
            }

    # Check password secure
    r = check_security(password=newpassword)
    if not r["success"]:
        return r
    

    user = findUserByID(userid, users=users)
    user.salt, user.hash = getSaltAndHash(password=newpassword)
    
    # Logout all other accounts
    res = logout_everywhere(sessionid=sessionid, sessionids=sessionids, db=db)
    if not res["success"]:
        return res


    newsessionid = login(
        username=user.username,
        password=newpassword,
        users=users,
        sessionids=sessionids,
        db=db
        )["data"]["sessionid"]
    return {
        "success": True,
        "response": "Password Updated",
        "data": {
            "sessionid": newsessionid
        }
    }