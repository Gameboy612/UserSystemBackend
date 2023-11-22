
from methods.action.settings.classes.privacy_settings import AccountPrivacySettings, privacy_settings
from methods.action.settings.init.create_privacy_settings import create_privacy_settings

def isPublic(userid: int) -> dict:
    """Successes if account is public, Fails if account is private or not exist.

    Args:
        userid (int): _description_

    Returns:
        dict: _description_
    """
    res = findPrivacySettingsFromUserID(userid)
    
    if not res["success"]:
        return res
    
    privacy = res["data"]["privacy_settings"]

    if privacy.profile_visibility == AccountPrivacySettings.Private:
        return {
            "success": False,
            "response": "Account is not Public.",
            "data": {
                "isPublic": False
            }
        }
    return {
            "success": True,
            "response": "",
            "data": {
                "isPublic": True
            }
        }

    


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

    p = privacy_settings.query.filter_by(userid=userid).first()
    if not p:
        return create_privacy_settings(userid)
    return {
        "success": True,
        "response": "",
        "data": {
            "privacy_settings": p
        }
    }