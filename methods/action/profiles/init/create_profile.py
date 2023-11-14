from sqlite3 import IntegrityError
from methods.action.profiles.classes.profiles import profiles
from db import db

def create_profile(userid: int) -> dict:
    """Creates a profile object for the associated userid.

    Args:
        userid (int): UserID of user.

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

    profile = profiles(userid)

    # Try to add to users
    db.session.add(profile)
    try:
        db.session.commit()
        return {
            "success": True,
            "response": "Profile created!",
            "data": {
                "profile": profile
            }
        }
    except IntegrityError:
        db.session.rollback()
        return {
            "success": False,
            "response": "Profile already Exists? This should not have happened...",
            "data": {}
        }

    