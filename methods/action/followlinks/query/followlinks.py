

from enum import Enum
from methods._utilities.obj_to_dict import obj_to_dict
from methods.action.profiles.init.create_profile import create_profile
from methods.user.login.query.sessionid import findUserIDBySessionID
from methods.action.followlinks.classes.followlinks import followlinks

class FollowStatus(Enum):
    NotFollowing = 0
    WaitingForApproval = 1
    Following = 2

def findFollowLinksFromUserID(
    userid: int,
    approved: bool = True
) -> dict:
    """Gets Follow links from UserID.

    Args:
        userid (int): Input UserID.

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "followings": followlinks,
                "followers": followlinks
            }
        }
        ```
    """

    followings = followlinks.query.filter_by(user_from=userid, approved=approved).all()
    followers = followlinks.query.filter_by(user_to=userid, approved=approved).all()
    return {
        "success": True,
        "response": "",
        "data": {
            "followings": followings,
            "followers": followers
        }
    }

def findFollowStatusBetweenUsers(user1: int, user2: int):
    """Gets Follow Status from UserID.

    Args:
        user1 (int): UserID from.
        user2 (int): UserID to.

    Returns:
        dict: Response, formatted as shown below.
        FollowStatus:
        0 - NotFollowing,
        1 - WaitingForApproval,
        2 - Following

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "forward": FollowStatus,
                "backward": FollowStatus
            }
        }
        ```
    """

    link_forward = followlinks.query.filter_by(user_from=user1, user_to=user2).first()
    link_backward = followlinks.query.filter_by(user_from=user2, user_to=user1).first()

    forward = FollowStatus.NotFollowing
    backward = FollowStatus.NotFollowing

    if forward:
        if link_forward.approved:
            forward = FollowStatus.Following
        else:
            forward = FollowStatus.WaitingForApproval
    if backward:
        if link_backward.approved:
            backward = FollowStatus.Following
        else:
            backward = FollowStatus.WaitingForApproval

    return {
        "success": True,
        "response": """
        FollowStatus:
        0 - NotFollowing,
        1 - WaitingForApproval,
        2 - Following
        """,
        "data": {
            "forward": forward,
            "backward": backward
        }
    }