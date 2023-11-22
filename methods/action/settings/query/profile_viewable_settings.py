
from methods.action.settings.classes.profile_viewable_settings import profile_viewable_settings
from methods.action.settings.init.create_profile_viewable_settings import create_profile_viewable_settings


def findProfileViewableSettingsFromUserID(
    userid: int
) -> dict:
    """Gets Privacy Settings for UserID.

    Args:
        userid (int): Input UserID.

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

    p = profile_viewable_settings.query.filter_by(userid=userid).first()
    if not p:
        return create_profile_viewable_settings(userid)
    return {
        "success": True,
        "response": "",
        "data": {
            "profile_viewable_settings": p
        }
    }