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
        case "main":
            from methods.action. import login
            response = login(
                username=data["username"],
                password=data["password"],
                users=users,
                sessionids=sessionids,
                db=db
            )
            return jsonify(response)
        
    
    return jsonify({
        "success": False,
        "response": "Method not found."
    })