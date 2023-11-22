from sqlite3 import IntegrityError
from db import db
from methods.action.settings.classes.profile_viewable_settings import profile_viewable_settings
from methods.user.login.query.user import findUserByID

def create_profile_viewable_settings(userid: int) -> dict:
    """Creates a profile_viewable_settings object for the associated userid.

    Args:
        userid (int): UserID of user.

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "profile_viewable_settings": profile_viewable_settings
            }
        }
        ```
    """

    if not findUserByID(userid):
        return {
            "success": False,
            "response": "User is not found.",
            "data": {}
        }
    p = profile_viewable_settings(userid)


    # Try to add to users
    db.session.add(p)
    try:
        db.session.commit()
        return {
            "success": True,
            "response": "Profile Viewable Settings created!",
            "data": {
                "profile_viewable_settings": p
            }
        }
    except IntegrityError:
        db.session.rollback()
        return {
            "success": False,
            "response": "Profile Viewable Settings Object already Exists? This should not have happened...",
            "data": {}
        }

    