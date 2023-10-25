from main import sessionids
from db import db
import datetime

from methods.user.login.password.calculate_hash import calculateHash

# SESSIONLIFE is to set the days required for the session to expire. (Default: 1 Day)
SESSIONLIFE = 1

def findSessionBySessionID(sessionid: str):
    """
    Gets Session object of given SessionID.

    Returns a dictionary object inluding the userid.

    Args:
        sessionid (str): Raw SessionID.

    Returns:
        dict: Response, formatted as shown below.
    
        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "session": sessionids
            }
        }
        ```
    """
    
    session = sessionids.query.filter_by(sessionid=calculateHash(sessionid.encode())).first()
    if not session:
        return {
            "success": False,
            "response": "Session not found.",
            "data": {}
        }
    
    t0 = session.lastused
    t1 = datetime.datetime.now()
    if (t1 - t0).days > SESSIONLIFE:
        db.session.delete(session)
        db.session.commit()
        return {
            "success": False,
            "response": "Your session expired.",
            "data": {}
        }
    session.accessedcount += 1
    db.session.commit()
    return {
        "success": True,
        "response": "",
        "data": {
            "session": session
        }
    }




def findSessionsBySessionID(sessionid: str):
    """Gets *ALL* SessionIDs of same UserID of given SessionID.

    Returns a dictionary object inluding the list of sessions.

    Args:
        sessionid (str): Raw SessionID.

    Returns:
        dict: Response, formatted as shown below.
    
        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "sessions": sessionids
            }
        }
        ```
    """

    r = findUserIDBySessionID(sessionid=sessionid)
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


def findUserIDBySessionID(sessionid: str) -> dict:
    """Gets UserID from SessionID.

    Returns a dictionary object inluding the userid.

    Args:
        sessionid (str): Raw SessionID.

    Returns:
        dict: Response, formatted as shown below.
    
        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "userid": int
            }
        }
        ```
    """

    r = findSessionBySessionID(sessionid=sessionid)
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