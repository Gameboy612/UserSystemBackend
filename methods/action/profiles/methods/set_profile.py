

from methods.action.profiles.query.profiles import findProfileFromSessionID
from db import db

def set_profile(
    sessionid: str,
    edited_data: dict,
) -> dict:
    """Sets the profile data of the sessionid holder.

    Args:
        sessionid (str): SessionID of user.
        edited_data (dict): New Profile Data of user.

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {}
        }
        ```
    """

    # Extracting response data.
    res = findProfileFromSessionID(sessionid)
    if not res["success"]:
        return res
    
    profile = res["data"]["profile"]

    for key in edited_data.keys():
        val = edited_data[key]
        print(profile, key, val)
        if hasattr(profile, key):
            setattr(profile, key, val)
            print(getattr(profile, key))
    
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return {
            "success": False,
            "response": "Database commit failed.",
            "data": {}
        }


    return {
        "success": True,
        "response": "Data successfully changed.",
        "data": {}
    }