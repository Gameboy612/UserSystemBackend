from methods._utilities.obj_to_dict import obj_to_dict
from methods.action.profiles.classes.profiles import profiles
from methods.action.profiles.query.profiles import findProfileFromSessionID


def get_profile(sessionid: int) -> dict:

    res = findProfileFromSessionID(sessionid)

    if not res["success"]:
        return res
    
    profile: profiles = res["data"]["profile"]
    
    return {
        "success": True,
        "response": "",
        "data": obj_to_dict(profile)
    }