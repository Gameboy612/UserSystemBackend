import bcrypt

from methods.user.login.query.sessionid import findUserIDBySessionID
from methods.user.login.query.user import findUserByID
from methods.user.login.password.verify_password import verify_userid_password
from methods.user.login.session.remove_session_id import logout_everywhere
from methods.user.login.session.get_session_id import login
from methods.user.login.password.calculate_hash import calculateHash
from methods.user.login.password.secure_password import check_security


def getSaltAndHash(password: str) -> (bytes, str):
    """Generates a *Salt* and returns the corresponding *Hash*.

    Args:
        password (str): The password you want to encrypt.

    Returns:
        bytes:  Salt.
        str:    Hash.
    """
    salt = bcrypt.gensalt()
    hash = calculateHash(password=password.encode("utf-8"), salt=salt)
    return salt, hash



def change_password(
        oldpassword: str,
        newpassword: str,
        sessionid: str,
        forcechange: bool = False, ) -> dict:
    """Change Password of user.

    Args:
        oldpassword (str): Raw Old Password.
        newpassword (str): Raw New Password.
        sessionid (str): Active SessionID.
        forcechange (bool, optional): Whether a force change is called. Defaults to False.

    Returns:
        dict: Response, formatted as shown below.
    
        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "sessionid": str
            }
        }
        ```
    """
    r = findUserIDBySessionID(sessionid=sessionid)

    if not r["success"]:
        return r

    userid = r["data"]["userid"]

    if (not verify_userid_password(userid=userid, password=oldpassword)):
        return {
            "success": False,
            "response": "Incorrect old password.",
            "data": {}
            }

    # Check password secure
    r = check_security(password=newpassword)
    if not r["success"]:
        return r
    

    user = findUserByID(userid)
    user.salt, user.hash = getSaltAndHash(password=newpassword)
    
    # Logout all other accounts
    res = logout_everywhere(sessionid=sessionid)
    if not res["success"]:
        return res


    newsessionid = login(
        username=user.username,
        password=newpassword
        )["data"]["sessionid"]
    return {
        "success": True,
        "response": "Password Updated",
        "data": {
            "sessionid": newsessionid
        }
    }