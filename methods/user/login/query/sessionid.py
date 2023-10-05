from main import sessionids

def findSessionBySessionID(sessionid: str):
    return sessionids.query.filter_by(sessionid=sessionid).first()

def findSessionsBySessionID(sessionid: str):
    return sessionids.query.filter_by(sessionid=sessionid).all()

def findUserIDBySessionID(sessionid: str):
    session = findSessionBySessionID(sessionid=sessionid)
    return session.userid