from flask import jsonify

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
        
    
    return jsonify({
        "success": False,
        "response": "Method not found."
    })