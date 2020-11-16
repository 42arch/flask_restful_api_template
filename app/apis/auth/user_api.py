# @Time : 2020/11/16 22:55
# @Author: dan
# @File : user_api.py
from flask_restful import Resource

from app.models.user import *


class UsersResource(Resource):
    def get(self):
        users = Users()
        return "get users"
