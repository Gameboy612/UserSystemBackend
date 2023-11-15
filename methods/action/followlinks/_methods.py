from flask import jsonify
from methods.action.followlinks.methods.change_followlinks import FollowManager as FollowManager

def run_method(
        method: list,
        data: dict
        ) -> dict:
    match method[0]:
        case "get_followlinks":
            from methods.action.followlinks.methods.get_followlinks import get_followlinks
            response = get_followlinks(
                userid=data["userid"],
                approved=True
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