from main import users

def findUserByUsername(username: str):
    return users.query.filter_by(username=username).first()


def findUserByID(id: int):
    return users.query.filter_by(_id=id).first()