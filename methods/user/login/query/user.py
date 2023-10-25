from main import users

def findUserByUsername(username: str, users: users) -> users:
    """Returns user by username.

    Args:
        username (str): Input username.
        users (users): The users object, forward this from `main.py`.

    Returns:
        users: Queried user.
    """
    return users.query.filter_by(username=username).first()


def findUserByID(id: int, users: users) -> users:
    """Returns user by userid.

    Args:
        id (int): Input UserID.
        users (users): The users object, forward this from `main.py`.

    Returns:
        users: Queried user.
    """
    return users.query.filter_by(_id=id).first()