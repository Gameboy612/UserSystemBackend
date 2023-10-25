from flask import jsonify

def run_method(
        method: list,
        data: dict,
        ) -> dict:
    match method[0]:
        case "login":
            from methods.user.login.session.get_session_id import login
            response = login(
                username=data["username"],
                password=data["password"],
            )
            return jsonify(response)
        
        case "register":
            from methods.user.register.create_user import register
            response = register(
                username=data["username"],
                password=data["password"],
            )
            return jsonify(response)
        
        case "change_password":
            from methods.user.login.password.change_password import change_password
            response = change_password(
                oldpassword=data["oldpassword"],
                newpassword=data["newpassword"],
                sessionid=data["sessionid"],
            )
            return jsonify(response)
        
        case "logout_everywhere":
            from methods.user.login.session.remove_session_id import logout_everywhere
            response = logout_everywhere(
                sessionid=data["sessionid"],
            )
            return jsonify(response)
    
    return jsonify({
        "success": False,
        "response": "Method not found."
    })