from db import db

DISPLAYNAME_LENGTH = 100
DESCRIPTION_LENGTH = 2200

MAX_WEBSITE_LENGTH = 100
MAX_EMAIL_LENGTH = 50
MAX_PHONE_NUMBER_LENGTH = 30

class followlinks(db.Model):
    __bind_key__ = 'followlinks'
    __tablename__ = 'followlinks'
    __table_args__ = {'extend_existing': True}

    _id = db.Column("id", db.Integer, primary_key=True)
    
    user_from = db.Column("user_from", db.Integer)
    user_to = db.Column("user_to", db.Integer)
    approved = db.Column("approved", db.Boolean)

    last_updated = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    def __init__(self, user_from, user_to, approved):
        self.user_from = user_from
        self.user_to = user_to
        self.approved = approved