from db import db

DISPLAYNAME_LENGTH = 100
DESCRIPTION_LENGTH = 2200

MAX_WEBSITE_LENGTH = 100
MAX_EMAIL_LENGTH = 50
MAX_PHONE_NUMBER_LENGTH = 30

class profiles(db.Model):
    __bind_key__ = 'profiles'
    __tablename__ = 'profiles'
    __table_args__ = {'extend_existing': True}

    _id = db.Column("id", db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=True)
    
    display_name = db.Column(db.String(DISPLAYNAME_LENGTH))

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_of_birth = db.Column(db.DateTime)

    description = db.Column(db.String(DESCRIPTION_LENGTH))
    gender = db.Column(db.String(30))
    
    primary_email_address = db.Column(db.String(MAX_EMAIL_LENGTH))
    secondary_email_address = db.Column(db.String(MAX_EMAIL_LENGTH))

    website_link = db.Column(db.String(MAX_WEBSITE_LENGTH))
    phone_number = db.Column(db.String(MAX_PHONE_NUMBER_LENGTH))

    last_updated = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    def __init__(self, userid):
        self.userid = userid