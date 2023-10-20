from flask import jsonify
from main import users, sessionids, db

def run_method(
        method: list,
        data: dict,
        users: users,
        sessionids: sessionids,
        db: db
        ) -> dict:
    match method[0]:
        case "get_main_data":
            from methods.action.get_main_data import get_main_data
            response = get_main_data(
                sessionid=data["sessionid"],
                users=users,
                sessionids=sessionids,
                db=db
            )
            return jsonify(response)
        
    
    return jsonify({
        "success": False,
        "response": "Method not found."
    })