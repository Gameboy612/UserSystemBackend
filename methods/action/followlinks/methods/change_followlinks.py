from methods.action.followlinks.classes.followlinks import followlinks
from methods.action.followlinks.methods.get_followlinks import get_followlinks
from methods.action.settings.classes.privacy_settings import AccountPrivacySettings
from methods.action.settings.query.privacy_settings import findPrivacySettingsFromUserID
from methods.user.login.query.sessionid import findUserIDBySessionID
from db import db

class FollowManager:
    def follow_user(sessionid: str, user_to: int) -> dict:
        if type(user_to) != int:
            return {
                "success": False,
                "response": "user_to should be an int.",
                "data": {}
            }

        # Extracting response data.
        res = findUserIDBySessionID(sessionid)
        if not res["success"]:
            return res
        user_from = res["data"]["userid"]

        # Find link
        links = get_followlinks(user_from)["data"]["followings"]
        if user_to in links:
            return {
                "success": False,
                "response": f"User already followed user {user_to}."
            }

        # Create link
        res = findPrivacySettingsFromUserID(user_to)
        
        if not res["success"]:
            return res
        
        privacy = res["data"]["privacy_settings"]

        isApproved = True
        if privacy.profile_visibility == AccountPrivacySettings.Private:
            isApproved = False
        
        followlink = followlinks(
            user_from=user_from,
            user_to=user_to,
            approved=isApproved
        )
        # Try to add to followlinks
        db.session.add(followlink)

        try:
            db.session.commit()
        except:
            return {
                "success": False,
                "response": "Unexpected Error. Followlink Commit failed.",
                "data": {}
            }
        return {
            "success": True,
            "response": "Successfully Followed User.",
            "data": {}
        }