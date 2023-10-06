from main import sessionids
import uuid

def findSessionBySessionID(sessionid: str, sessionids: sessionids):
    return sessionids.query.filter_by(sessionid=uuid.UUID(sessionid)).first()

def findSessionsBySessionID(sessionid: str, sessionids: sessionids):
    r = findUserIDBySessionID(sessionid=sessionid, sessionids=sessionids)
    if not r["success"]:
        return r
    
    userid = r["data"]["userid"]

    return {
        "success": True,
        "response": "",
        "data": {
            "sessions": sessionids.query.filter_by(userid=userid).all()
        }
    }

def findUserIDBySessionID(sessionid: str, sessionids: sessionids) -> dict:
    session = findSessionBySessionID(sessionid=sessionid, sessionids=sessionids)
    if not session:
        return {
            "success": False,
            "response": "Session not found!",
            "data": {}
        }
    return {
            "success": True,
            "response": "",
            "data": {
                "userid": session.userid
            }
        }