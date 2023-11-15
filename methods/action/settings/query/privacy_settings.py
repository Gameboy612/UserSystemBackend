
from methods.action.settings.classes.privacy_settings import privacy_settings
from methods.action.settings.init.create_privacy_settings import create_privacy_settings


def findPrivacySettingsFromUserID(
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
                "privacy_settings": privacy_settings
            }
        }
        ```
    """

    p = privacy_settings.query.filter_by(_id=userid).first()
    if not p:
        return create_privacy_settings(userid)
    return {
        "success": True,
        "response": "",
        "data": {
            "privacy_settings": p
        }
    }