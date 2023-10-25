from flask import jsonify

def run_method(
        method: list,
        data: dict
        ) -> dict:
    match method[0]:
        case "get_profile":
            from methods.action.get_profile import get_profile
            response = get_profile(
                sessionid=data["sessionid"]
            )
            return jsonify(response)
        
    
    return jsonify({
        "success": False,
        "response": "Method not found."
    })