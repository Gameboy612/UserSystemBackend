from db import db
from methods.action.settings.classes.privacy_settings import AccountPrivacySettings



class profile_viewable_settings(db.Model):
    __bind_key__ = 'settings'
    __tablename__ = 'profile_viewable_settings'
    __table_args__ = {'extend_existing': True}

    _id = db.Column("id", db.Integer, primary_key=True)
    userid = db.Column("userid", db.Integer, unique=True)
    
    display_name = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Public)

    first_name = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Public)
    last_name = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Public)
    date_of_birth = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Private)

    description = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Public)
    gender = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Public)
    
    primary_email_address = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Hidden)
    secondary_email_address = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Hidden)

    website_link = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Private)
    phone_number = db.Column(db.Enum(AccountPrivacySettings), default=AccountPrivacySettings.Hidden)

    last_updated = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    def __init__(self, userid):
        self.userid = userid