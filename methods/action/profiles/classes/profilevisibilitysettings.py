from db import db
import enum


class AccountPrivacySettings(enum.Enum):
    Public = 0
    Private = 1

class ReachabilitySettings(enum.Enum):
    Everyone = 0
    PeopleYouFollow = 1
    Disallow = 2


class privacy_settings(db.Model):
    __tablename__ = 'privacy_settings'
    __table_args__ = {'extend_existing': True}
    
    _id = db.Column("id", db.Integer, db.ForeignKey('users.id'))
    
    profile_visibility = db.Column(db.Enum(AccountPrivacySettings))
    
    tagability = db.Column(db.Enum(ReachabilitySettings))

    def __init__(
            self,
            _id: int,
            profile_visibility: AccountPrivacySettings,
            tagability: ReachabilitySettings
            ):
        self._id = _id
        self.profile_visibility = profile_visibility
        self.tagability = tagability