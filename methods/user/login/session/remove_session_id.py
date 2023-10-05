import uuid
from methods.user.login.query.sessionid import findSessionBySessionID, findSessionsBySessionID
from main import db

def logout(sessionid: uuid) -> dict:
    session = findSessionBySessionID(sessionid=sessionid)
    session.delete()
    db.session.commit()


def logout_everywhere(sessionid: uuid) -> dict:
    sessions = findSessionsBySessionID(sessionid=sessionid)
    for session in sessions:
        session.delete()
    db.session.commit()