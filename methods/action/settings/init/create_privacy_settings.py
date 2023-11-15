from sqlite3 import IntegrityError
from db import db
from methods.action.settings.classes.privacy_settings import privacy_settings

def create_privacy_settings(userid: int) -> dict:
    """Creates a privacy_settings object for the associated userid.

    Args:
        userid (int): UserID of user.

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "privacy_settings": privacy_settings
            }
        }
        ```
    """

    p = privacy_settings(userid)

    # Try to add to users
    db.session.add(p)
    try:
        db.session.commit()
        return {
            "success": True,
            "response": "Privacy Settings created!",
            "data": {
                "privacy_settings": p
            }
        }
    except IntegrityError:
        db.session.rollback()
        return {
            "success": False,
            "response": "Privacy Settings Object already Exists? This should not have happened...",
            "data": {}
        }

    