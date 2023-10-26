

from methods._utilities.obj_to_dict import obj_to_dict
from methods.action.profiles.init.create_profile import create_profile
from methods.user.login.query.sessionid import findUserIDBySessionID
from methods.action.profiles.classes.profiles import profiles

def findProfileFromUserID(
    userid: int
) -> dict:
    """Gets Profile from UserID.

    Args:
        userid (int): Input UserID.

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "profile": profiles
            }
        }
        ```
    """

    profile = profiles.query.filter_by(_id=userid).first()
    if not profile:
        return create_profile(userid)
    return {
        "success": True,
        "response": "",
        "data": {
            "profile": profile
        }
    }


def findProfileFromSessionID(
    sessionid: str
) -> dict:
    """Gets Profile from SessionID.

    Returns a dictionary object inluding the profile.

    Args:
        sessionid (str): Raw SessionID.
        sessionids (sessionids): The sessionids class, forward this from `main.py`.
        db (db): The db object, forward this from `main.py`.
        profiles (profiles): The profiles class, forward this from `main.py`.

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "profile": profiles
            }
        }
        ```
    """


    r = findUserIDBySessionID(sessionid)

    if not r["success"]:
        return {
            "success": False,
            "response": r["response"],
        }

    userid = r["data"]["userid"]
    
    return findProfileFromUserID(userid)