import bcrypt

from methods.user.login.query.sessionid import findUserIDBySessionID
from methods.user.login.query.user import findUserByID
from methods.user.login.get_session_id import calculateHash
from methods.user.login.password.verify_password import verify_userid_password

def getSaltAndHash(password: str) -> (bytes, str):
    salt = bcrypt.gensalt()
    hash = calculateHash(password=password.encode("utf-8"), salt=salt)
    return salt, hash



def change_password(
        oldpassword: str,
        newpassword: str,
        sessionid: str,
        forcechange: bool = False ) -> dict:

    userid = findUserIDBySessionID(sessionid=sessionid)
    
    if forcechange or not verify_userid_password(userid=userid, password=oldpassword):
        return {
            "success": False,
            "response": "Incorrect old password."
            }

    user = findUserByID(userid)
    user.salt, user.hash = getSaltAndHash(password=newpassword)
    