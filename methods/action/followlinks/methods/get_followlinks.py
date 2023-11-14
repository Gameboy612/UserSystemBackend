
from methods.action.followlinks.classes.followlinks import followlinks
from methods.action.followlinks.query.followlinks import findFollowLinksFromUserID


def get_followlinks(userid: int) -> dict:
    """Gets the followers and followings of the user as two list of ints, corresponding to each user.

    Args:
        userid (int): UserID of user.

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
    res = findFollowLinksFromUserID(userid)

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