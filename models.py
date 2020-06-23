from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, id, username, email, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
