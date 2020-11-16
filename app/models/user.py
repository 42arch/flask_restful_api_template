# @Time : 2020/11/17 0:00
# @Author: dan
# @File : user.py
from app.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(128))