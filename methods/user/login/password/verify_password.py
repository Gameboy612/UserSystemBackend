from methods.user.login.password.calculate_hash import calculateHash
from methods.user.login.query.user import findUserByID, findUserByUsername

from main import users

def verify_username_password(username: str, password: str) -> bool:
    """Verify if the username and password pair matches.

    Args:
        username (str): Input username.
        password (str): Raw Password.

    Returns:
        bool: Whether the username and password pair match
    """
    user = findUserByUsername(username)
    calchash = calculateHash(password.encode("utf-8"), user.salt)
    return calchash == user.hash


def verify_userid_password(userid: int, password: str) -> bool:
    """Verify if the userid and password pair matches.

    Args:
        userid (int): Input userid.
        password (str): Raw Password.

    Returns:
        bool: Whether the userid and password pair match
    """
    user = findUserByID(userid)
    return verify_username_password(
        username=user.username,
        password=password
    )