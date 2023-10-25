from main import users

def findUserByUsername(username: str) -> users:
    """Returns user by username.

    Args:
        username (str): Input username.

    Returns:
        users: Queried user.
    """
    return users.query.filter_by(username=username).first()


def findUserByID(id: int) -> users:
    """Returns user by userid.

    Args:
        id (int): Input UserID.

    Returns:
        users: Queried user.
    """
    return users.query.filter_by(_id=id).first()