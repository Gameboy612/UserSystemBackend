from main import users

def findUserByUsername(username: str, users: users):
    return users.query.filter_by(username=username).first()


def findUserByID(id: int, users: users):
    return users.query.filter_by(_id=id).first()