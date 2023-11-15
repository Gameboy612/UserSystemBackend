from flask import jsonify
from methods.action.followlinks.methods.change_followlinks import FollowManager as FollowManager

def run_method(
        method: list,
        data: dict
        ) -> dict:
    match method[0]:
        case "get_profile":
            from methods.action.profiles.methods.get_profile import get_profile
            response = get_profile(
                sessionid=data["sessionid"]
            )
            return jsonify(response)
        case "set_profile":
            from methods.action.profiles.methods.set_profile import set_profile
            response = set_profile(
                sessionid=data["sessionid"],
                edited_data=data["edited_data"]
            )
            return jsonify(response)
        case "get_followlinks":
            from methods.action.followlinks.methods.get_followlinks import get_followlinks
            response = get_followlinks(
                userid=data["userid"]
            )
            return jsonify(response)
        case "get_relation":
            from methods.action.followlinks.query.followlinks import getFollowStatusBetweenUsers
            response = getFollowStatusBetweenUsers(data["userid1"], data["userid2"])
            return jsonify(response)
        
        case "follow_user":
            response = FollowManager.follow_user(data["sessionid"], data["userid"])
            return jsonify(response)
    
    return jsonify({
        "success": False,
        "response": "Method not found."
    })