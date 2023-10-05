from methods.user.login.password.change_password import calculateHash
from methods.user.login.query.user import findUserByID, findUserByUsername

def verify_username_password(username: str, password: str) -> bool:
    user = findUserByUsername(username)
    return calculateHash(password.encode("utf-8"), user.salt) == user.hash


def verify_userid_password(userid: str, password: str) -> bool:
    user = findUserByID(userid)
    return calculateHash(password.encode("utf-8"), user.salt) == user.hash