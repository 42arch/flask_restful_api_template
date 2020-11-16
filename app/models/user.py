# @Time : 2020/11/16 22:50
# @Author: dan
# @File : user.py
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    username = db.Column(db.String(32), unique=True)
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(256))
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')
    #
    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)
    #
    # def __repr__(self):
    #     return '<User %r>' % self.username
