
from methods.action.followlinks.classes.followlinks import followlinks
from methods.action.followlinks.query.followlinks import getFollowLinksFromUserID


def get_followlinks(userid: int, approved: bool | int = -1) -> dict:
    """Gets the followers and followings of the user as two list of ints, corresponding to each user.

    Args:
        userid (int): UserID of user.
        approved (bool | int): Whether non-approved follows should be returned. (If -1, then returns all followlinks, including not approved)

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "followings": [1, 2, 3],
                "followers": [1, 3]
            }
        }
        ```
    """
    res = getFollowLinksFromUserID(userid, approved=approved)

    if not res["success"]:
        return res
    
    
    # Get list of users
    followings = [x.user_to for x in res["data"]["followings"]]
    followers = [x.user_from for x in res["data"]["followers"]]
    return {
        "success": True,
        "response": "",
        "data": {
            "followings": followings,
            "followers": followers
        }
    }