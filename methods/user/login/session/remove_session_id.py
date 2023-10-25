import uuid
from methods.user.login.query.sessionid import findSessionBySessionID, findSessionsBySessionID
from main import sessionids
from db import db

def logout(sessionid: uuid) -> dict:
    session = findSessionBySessionID(sessionid=sessionid)
    if not session:
        return {
            "success": False,
            "response": "SessionID not found."
        }
    db.session.delete(session)
    db.session.commit()
    return {
        "success": True,
        "response": "Session Key Deleted."
    }


def logout_everywhere(sessionid: uuid) -> dict:
    r = findSessionsBySessionID(sessionid=sessionid)

    if not r["success"]:
        return r

    sessions = r["data"]["sessions"]

    if not sessions:
        return {
            "success": False,
            "response": "SessionID not found."
        }
    for i in sessions:
        db.session.delete(i)
    db.session.commit()
    return {
        "success": True,
        "response": "All Related Session Keys Deleted."
    }