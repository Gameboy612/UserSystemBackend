import bcrypt

from methods.user.login.query.sessionid import findUserIDBySessionID
from methods.user.login.query.user import findUserByID
from methods.user.login.session.get_session_id import calculateHash


def getSaltAndHash(password: str) -> (bytes, str):
    salt = bcrypt.gensalt()
    hash = calculateHash(password=password.encode("utf-8"), salt=salt)
    return salt, hash



def change_password(oldpassword: str, newpassword: str, sessionid: str) -> dict:
    

    userid = findUserIDBySessionID(sessionid=sessionid)
    user = findUserByID(userid)

    user.salt, user.hash = getSaltAndHash(password=newpassword)
    