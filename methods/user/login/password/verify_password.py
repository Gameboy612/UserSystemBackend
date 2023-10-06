from methods.user.login.password.calculate_hash import calculateHash
from methods.user.login.query.user import findUserByID, findUserByUsername

from main import users

def verify_username_password(username: str, password: str, users: users) -> bool:
    user = findUserByUsername(username, users=users)
    calchash = calculateHash(password.encode("utf-8"), user.salt)
    return calchash == user.hash


def verify_userid_password(userid: int, password: str, users: users) -> bool:
    user = findUserByID(userid, users=users)
    return verify_username_password(
        username=user.username,
        password=password,
        users=users
    )