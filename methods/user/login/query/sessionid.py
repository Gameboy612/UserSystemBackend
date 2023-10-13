from main import sessionids
import uuid
import datetime

SESSIONLIFE = 1

def findSessionBySessionID(sessionid: str, sessionids: sessionids):
    session = sessionids.query.filter_by(sessionid=uuid.UUID(sessionid)).first()
    if not session:
        return {
            "success": False,
            "response": "Session not found.",
            "data": {}
        }
    
    t0 = session.lastused
    t1 = datetime.datetime.now().date()
    print(t0)
    print(t1)
    if (True):
        return {
            "success": False,
            "response": "Your session expired.",
            "data": {}
        }
    return {
        "success": True,
        "response": "",
        "data": {
            "session": session
        }
    }
        

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
    r = findSessionBySessionID(sessionid=sessionid, sessionids=sessionids)
    if not r["success"]:
        return r
    session = r["data"]["session"]

    return {
            "success": True,
            "response": "",
            "data": {
                "userid": session.userid
            }
        }