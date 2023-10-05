import bcrypt
import base64
import hashlib

from methods.user.login.query.sessionid import findUserIDBySessionID
from methods.user.login.query.user import findUserByID
from methods.user.login.password.verify_password import verify_userid_password
from methods.user.login.session.remove_session_id import logout_everywhere
from methods.user.login.session.get_session_id import login

def calculateHash(password: bytes, salt: bytes) -> str:
    '''
    Returns the hash of the password
    '''
    return bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(password).digest()),
        salt
    )


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
            "response": "Incorrect old password.",
            "data": {}
            }

    user = findUserByID(userid)
    user.salt, user.hash = getSaltAndHash(password=newpassword)
    
    # Logout all other accounts
    logout_everywhere(userid)

    newsessionid = login(username=user.username, password=user.newpassword)["data"]["sessionid"]
    return {
        "success": True,
        "response": "Password Updated",
        "data": {
            "sessionid": newsessionid
        }
    }