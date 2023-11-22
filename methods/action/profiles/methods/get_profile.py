from methods._utilities.obj_to_dict import obj_to_dict
from methods.action.followlinks.query.followlinks import FollowStatus, getFollowStatusBetweenUsers
from methods.action.profiles.classes.profiles import profiles
from methods.action.profiles.query.profiles import findProfileFromUserID
from methods.action.settings.classes.privacy_settings import AccountPrivacySettings as _aps
from methods.action.settings.classes.profile_viewable_settings import profile_viewable_settings
from methods.action.settings.query.privacy_settings import isPublic
from methods.action.settings.query.profile_viewable_settings import findProfileViewableSettingsFromUserID
from methods.user.login.query.sessionid import findUserIDBySessionID


def get_profile(sessionid: str, userid: int = -1) -> dict:
    # Gets the caller's userid.
    res = findUserIDBySessionID(sessionid)
    if not res["success"]:
        return res
    callerid = res["data"]["userid"]

    # Get self profile if finding self profile.
    if userid == callerid:
        userid = -1

    # Get Profile of self.
    if userid == -1:
        res_profile = findProfileFromUserID(callerid)
        if not res_profile["success"]:
            return res_profile
        profile = res_profile["data"]["profile"]

        return {
            "success": True,
            "response": "",
            "data": obj_to_dict(profile)
        }
    
    # Get Profile of others (and check profile viewable settings).
    res_profile = findProfileFromUserID(userid)    
    res_settings = findProfileViewableSettingsFromUserID(userid)
    
    if not res_profile["success"]:
        return res_profile
    if not res_settings["success"]:
        return res_settings
    
    # Extract profile and settings.
    profile: profiles = res_profile["data"]["profile"]
    profile_viewable_setting: profile_viewable_settings = res_settings["data"]["profile_viewable_settings"]
    
    # Convert profile to dict
    profile_dict = obj_to_dict(profile)

    # Extracting response data.
    res = getFollowStatusBetweenUsers(callerid, userid)
    if not res["success"]:
        return res
    
    follow_status = res["data"]["forward"]

    for key in profile_dict:
        setting = getattr(profile_viewable_setting, key)
        if setting == _aps.Hidden:
            profile_dict[key] = None
        elif setting == _aps.Private and follow_status != FollowStatus.Following.value:
            profile_dict[key] = None

    return {
        "success": True,
        "response": "",
        "data": {
            "profile": profile_dict
        }
    }