from main import sessionids

def findUserIDBySessionID(sessionid: str):
    session = sessionids.query.filter_by(sessionid=sessionid).first()
    return session.userid
